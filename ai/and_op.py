# 과제 3 - and_op.py
import numpy as np

x1 = np.array([0, 0])
x2 = np.array([0, 1])
x3 = np.array([1, 0])
x4 = np.array([1, 1])

W = np.array([[0, 0], [1, 1]])
b = np.array([1, 0])

def f(x_1by2):
    return np.argmax(x_1by2)

print(f(W.dot(x1) + b))  # f(w*x1 + b) = 0
print(f(W.dot(x2) + b))  # f(w*x2 + b) = 0
print(f(W.dot(x3) + b))  # f(w*x3 + b) = 0
print(f(W.dot(x4) + b))  # f(w*x4 + b) = 1