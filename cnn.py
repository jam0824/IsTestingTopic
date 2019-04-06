import chainer
import chainer.functions as F
import chainer.links as L


class NMIST_Conv_NN(chainer.Chain):
    def __init__(self, n):
        super(NMIST_Conv_NN, self).__init__()
        with self.init_scope():
            self.conv1 = L.Convolution2D(1, 16, ksize=3)
            self.conv2 = L.Convolution2D(16, 16, ksize=2)
            self.linear1 = L.Linear(576, n)
    def __call__(self, x, t=None, train=True):
        h1 = self.conv1(x)
        h2 = F.relu(h1)
        h3 = F.max_pooling_2d(h2, 2)
        h4 = self.conv2(h3)
        h5 = F.max_pooling_2d(h4, 2)
        h6 = self.linear1(h5)
        return F.softmax_cross_entropy(h6, t) if train else F.softmax(h6)