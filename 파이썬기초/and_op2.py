# 과제 3 - and_op.py
import numpy as np

x1 = np.array([0, 0])
x2 = np.array([0, 1])
x3 = np.array([1, 0])
x4 = np.array([1, 1])

W = np.array([[0.6, 0.6], [1, 1]])
b = np.array([1, 0.5])

# W[1][0]-W[0][0] = α
# W[1][1]-W[0][1] = β
# b[0]-b[1] = γ 라 할 때,
# γ < α + β 인 모든 W와 b에 대해 and 연산이 성립한다.

def f(x_1by2):
    return np.argmax(x_1by2)

print(f(W.dot(x1) + b))  # f(w*x1 + b) = 0
print(f(W.dot(x2) + b))  # f(w*x2 + b) = 0
print(f(W.dot(x3) + b))  # f(w*x3 + b) = 0
print(f(W.dot(x4) + b))  # f(w*x4 + b) = 1