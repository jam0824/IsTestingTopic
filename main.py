#coding: UTF-8
import use_brain
import sys
import codecs


a = use_brain.use_brain()
text = 'オレはテストやQAのプロであって、プレゼンのプロではない。'
args = sys.argv
if args[1] != '':
    text = args[1]


ans_cnt = 0
print(text)
model = 'akiyama.hdf5'
model_ans = a.use_brain(text, model)
if model_ans:
    ans_cnt = ans_cnt + 1
print('a_model : '+str(model_ans))

model = 'nishi.hdf5'
model_ans = a.use_brain(text, model)
if model_ans:
    ans_cnt = ans_cnt + 1
print('n_model : '+str(model_ans))

model = 'teacher.hdf5'
model_ans = a.use_brain(text, model)
if model_ans:
    ans_cnt = ans_cnt + 1
print('c_model : '+str(model_ans))

print('賛成：' + str(ans_cnt) + '　反対： ' + str(3 - ans_cnt))
if ans_cnt >= 2:
    print('結果：テストっぽい話です')
else:
    print('結果：テストっぽくないです')