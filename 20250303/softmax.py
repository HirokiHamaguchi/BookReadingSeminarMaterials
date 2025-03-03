import numpy as np


# 通常のSoftmax関数（オーバーフローの危険あり）
def softmax_normal(x):
    exp_x = np.exp(x)  # 直接指数関数を適用（オーバーフローの危険あり）
    return exp_x / np.sum(exp_x)


# 数値安定化されたSoftmax関数
def softmax_stable(x):
    m = np.max(x)  # 最大値を引いてオーバーフローを防止
    exp_x = np.exp(x - m)
    return exp_x / np.sum(exp_x)


# テスト用データ（大きな値を含む）
for x in [
    np.array([10, 11, 12]),
    np.array([100, 101, 102]),
    np.array([1000, 1001, 1002]),
]:
    print(f"{x=}")

    # 通常のSoftmaxを試す（オーバーフローが発生する可能性大）
    try:
        normal_result = softmax_normal(x)
    except OverflowError:
        normal_result = "OverflowError!"

    # 数値安定化されたSoftmaxを試す
    stable_result = softmax_stable(x)

    print(normal_result, stable_result)  # 結果表示


'''
PS C:\Users\hirok\Documents\University\BookReadingSeminarMaterials> & C:/Users/hirok/anaconda3/python.exe c:/Users/hirok/Documents/University/BookReadingSeminarMaterials/20250303/softmax.py
x=array([10, 11, 12])
[0.09003057 0.24472847 0.66524096] [0.09003057 0.24472847 0.66524096]
x=array([100, 101, 102])
[0.09003057 0.24472847 0.66524096] [0.09003057 0.24472847 0.66524096]
x=array([1000, 1001, 1002])
c:\Users\hirok\Documents\University\BookReadingSeminarMaterials\20250303\softmax.py:6: RuntimeWarning: overflow encountered in exp
  exp_x = np.exp(x)  # 直接指数関数を適用（オーバーフローの危険あり）
c:\Users\hirok\Documents\University\BookReadingSeminarMaterials\20250303\softmax.py:7: RuntimeWarning: invalid value encountered in divide
  return exp_x / np.sum(exp_x)
[nan nan nan] [0.09003057 0.24472847 0.66524096]
'''


'''
>>> math.e ** -1000
0.0
>>> math.e ** -100
3.7200759760208555e-44
>>> math.e ** -10
4.5399929762484875e-05
>>> math.e ** +10
22026.465794806703
>>> math.e ** +100
2.6881171418161212e+43
>>> math.e ** +1000
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: (34, 'Result too large')
'''