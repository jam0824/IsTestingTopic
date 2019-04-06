import unittest
import mecabclass

class Test_mecabをつかってわかちわけができる(unittest.TestCase):
    def test_わかちわけを確認する(self):
        m = mecabclass.mecabclass()
        actual = m.wakachi("テストエンジニアにも資格があるのか")
        expected = ['テスト', 'エンジニア', 'に', 'も', '資格', 'が', 'ある', 'の', 'か']

        self.assertEqual(expected, actual)

    def test_word_listをlistに読み込む(self):
        m = mecabclass.mecabclass()
        actual = m.load_words_list('test_list_file.txt')
        expected =  ['エンジニア', 'テスト']
        self.assertEqual(expected, actual)

    def test_単語リストを番号にして返す(self):
        m = mecabclass.mecabclass()
        actual = m.numbering(['エンジニア','テスト'])
        expected = [0, 1]
        self.assertEqual(expected, actual)

    def test_文章を投げると数字になって帰ってくる(self):
        m = mecabclass.mecabclass()
        #print(m.get_number_list("仕様書でも、設計書でも、プログラムコードでも何でも、一文字10円でレビューしますっていう商売はどうだろう？"))
        actual = m.get_number_list("テストエンジニアにも資格があるのか")
        expected = 100
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()