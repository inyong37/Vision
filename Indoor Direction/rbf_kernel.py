'''
Inyong Hwang


# Python
# array call: https://stackoverflow.com/questions/3582601/how-to-call-an-element-in-a-numpy-array
# Matlab to Python: https://docs.scipy.org/doc/numpy-1.15.0/user/numpy-for-matlab-users.html
# Matlab to Python: http://mathesaurus.sourceforge.net/matlab-numpy.html
# numpy.arange: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.arange.html
# Matalb
# RBF Kernel: https://kr.mathworks.com/matlabcentral/fileexchange/63033-svm-using-various-kernels
# Function: https://kr.mathworks.com/help/matlab/ref/function.html
# ETC
# CS231n Korean: http://aikorea.org/cs231n/python-numpy-tutorial/
'''

import numpy as np
import scipy as sp
import math as m
import matplotlib.pyplot as plt

def func_1(k):
    k = k + 1e-6*np.identity(n)
    ck = np.linalg.cholesky(k)
    f = ck*np.random.standard_normal(n,)
    return f

def func_2(x, i, j, constant, gamma):
    k[i, j] = constant * m.exp(((-1) * (abs(x[i] - x[j])) ** 2) / gamma)
    return k[i, j]

x = np.arange(-10, 10, 0.2)
n = np.size(x)
k = np.zeros((n, n))
constant = 1
constnat = constant**2
sigma = 1
gamma = 2*(sigma**2)

'''
for i in range(1, n+1):
    for j in range(1, n+1):
        for sigma in range(1, 6):
            for constant in range(1, 6):
                k[i,j] = constant*m.exp(((-1)*(x[i]-x[j])^2)/gamma)
'''
for i in range(1, n):
    for j in range(1, n):
        # k[i, j] = constant * m.exp(((-1) * (abs(x[i] - x[j])) ** 2) / gamma)
        k[i, j] = func_2(x, i, j, constant, gamma)

f = func_1(k)

plt.plot(x, f)
plt.show()
