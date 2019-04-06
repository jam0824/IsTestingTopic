import chainer
import chainer.functions as F
import chainer.links as L
from chainer import training, datasets, iterators, optimizers
from chainer.training import extensions
import numpy as np
import mecabclass
import cnn

class use_brain:
    def use_brain(self, text, model_name):
        cp = np
        model = cnn.NMIST_Conv_NN(2)
        chainer.serializers.load_hdf5(model_name, model)
        m = mecabclass.mecabclass()
        tmp = [[m.makeSentenceMatrix(28, 28, m.get_number_list(text))]]
        npData = (cp.array(tmp)).astype(cp.float32)
        result = model(npData, train=False)
        ans = int(np.argmax(result.data, axis=1))

        '''
        for i in range(len(result.data[0])):
            print(str(i) + '\t' + str(result[0][i]))
        '''
        
        if ans == 1:
            #print("It's a testing sentence!")
            return True
        else:
            #print("It's not.")
            return False