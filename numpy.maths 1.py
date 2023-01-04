'''
DATE:31TH DEC 2022
DAY: SATURDAY
TOPIC: ERROR_HANDLING
AUTHOR:RAMA BHARGAvi
'''
import numpy as np
t = [x for x in range(0,101,2)]
u = np.array(t)
print(u)
v = np.arange(0,101,2)
print(v)
w = np.array([1,2,3,4,5])
x = np.array([1,3,2,4,5])
print(np.where(w == x))
z = np.full((3, 3), 8)
print(z)
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
b = np.array([[2,3,4],
              [5,6,7],
              [8,9,10]])
c = a@b
d = np.matmul(a, b)
print(c)
print(d)
e = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
f = e.T
print(f)
