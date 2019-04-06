import chainer
import chainer.functions as F
import chainer.links as L
from chainer import training, datasets, iterators, optimizers
from chainer.training import extensions
import numpy as np
import mecabclass
import codecs
import cnn

batch_size = 10
uses_device = -1

class brain:
    def combine_test_data(self,pass_file_name, ng_file_name, m):
        teach_list, teach_ans = self.read_and_change_text(ng_file_name, 0, m)
        teach_pass_list, teach_pass_ans = self.read_and_change_text(pass_file_name, 1, m)
        teach_list.extend(teach_pass_list)
        teach_ans.extend(teach_pass_ans)
        return teach_list, teach_ans


    def read_and_change_text(self, file_name, ans_no, m):
        line_list = []
        ans_list = []
        file = codecs.open(file_name, 'r', 'utf8')
        line = file.readline()
        while line:
            line = line.replace('\n', '')
            if line != '':
                line_list.append(m.get_number_list(line))
                ans_list.append(ans_no)
            line = file.readline()
        file.close()
        return line_list, ans_list

    def make_test_data(self, test_list, test_ans, m):
        #データ成型
        testData = []
        cnt = 0
        for sentence in test_list:
            data = []
            #文章を28x28のマトリクス化
            y = m.makeSentenceMatrix(28, 28, sentence)
            #無理やり成型
            data.append(y)
            #float32の行列に変更
            npData = (np.array(data)).astype(np.float32)
            #答えをくっつけて教師データ化
            testData.append((npData, test_ans[cnt]))
            cnt += 1
        return testData

    def start(self, name, study_num):
        m = mecabclass.mecabclass()
        #教師データの作成
        teach_list, teach_ans = self.combine_test_data(name+'_pass.txt', name+'_ng.txt', m) 
        teachData = self.make_test_data(teach_list, teach_ans, m)

        #テストデータの作成
        test_list, test_ans = self.combine_test_data('test_pass.txt', 'test_ng.txt', m) 
        testData = self.make_test_data(test_list, test_ans, m)

        model = cnn.NMIST_Conv_NN(2)

        train_iter = iterators.SerialIterator(teachData, batch_size, shuffle=True)
        test_iter = iterators.SerialIterator(testData, batch_size, repeat=False, shuffle=False)

        optimizer = optimizers.Adam()
        optimizer.setup(model)

        updater = training.StandardUpdater(train_iter, optimizer, device=uses_device)
        trainer = training.Trainer(updater, (study_num, 'epoch'), out="result")

        trainer.extend(extensions.Evaluator(test_iter, model, device=uses_device))
        trainer.extend(extensions.ProgressBar())

        trainer.run()
        chainer.serializers.save_hdf5(name+'.hdf5', model)

