import MeCab
import sys
import codecs

WORD_LIST_FILE_NAME = 'words_list.txt'
MAX_LENGTH = 784

class mecabclass:
    def __init__(self):
        self.words_list = self.load_words_list(WORD_LIST_FILE_NAME)

    def get_number_list(self, text):
        wakachi = self.wakachi(text)
        words = self.numbering(wakachi)
        return self.fill_zero(words)

    def wakachi(self, text):
        m = MeCab.Tagger("-Owakati")
        return_value = (m.parse(text)).strip()
        return return_value.split(' ')

    def load_words_list(self, file_name):
        words_list = []
        file = codecs.open(file_name, 'r', 'utf8')
        line = file.readline()
        while line:
            words_list.append(line.strip())
            line = file.readline()
        file.close()
        return words_list

    def numbering(self, target_word_list):
        number_list = []
        parameter = len(self.words_list)
        for word in target_word_list:
            if word not in self.words_list:
                number = len(self.words_list) / parameter
                number_list.append(number)
                self.words_list.append(word)
                self.save_add_line(WORD_LIST_FILE_NAME, word)
            else:
                number = self.words_list.index(word) / parameter
                number_list.append(number)
        return number_list

    def fill_zero(self, words):
        length = len(words)
        n = MAX_LENGTH - length
        cnt = 0
        for i in range(n):
            words.append(words[cnt])
            cnt = cnt + 1
            if cnt > length:
                cnt = 0
        return words


    def save_add_line(self, file_name, word):
        with codecs.open(file_name, 'a', 'utf-8') as f:
            print(word, file=f)

    def makeSentenceMatrix(self, x, y, sentence):
        sentenceLength = len(sentence)
        cnt = 0
        matrix = []
        for i in range(y):
            line = []
            for j in range(x):
                line.append(sentence[cnt])
                cnt += 1
                if cnt == sentenceLength:
                    cnt = 0
            matrix.append(line)
        return matrix

