import numpy as np

# average 2 matrix

a = np.array([[1, 2, 3], [2, 3, 4]])
b = np.array([[2, 3, 4], [3, 4, 5]])

ab = [a,b]

np.average(ab,axis=0)
# array([[ 1.5,  2.5,  3.5],
#       [ 2.5,  3.5,  4.5]])
