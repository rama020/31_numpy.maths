'''
DATE:31TH DEC 2022
DAY: SATURDAY
TOPIC: ERROR_HANDLING
AUTHOR:RAMA BHARGAvi
'''
import numpy as np
a = np.array([[10,20,30],
              [40,50,60]])
b = np.array([[1,2,3],
              [4,5,6]])
print(a,b)
c = a + b
d = a * b
e = a - b
f = a * b
print(c)
print(d)
print(e)
print(f)  
g = np.eye(6)
print(g)
h = np.eye(3,dtype=int)
print(h)
h = np.array([x for x in range(9)])
i = h.reshape((3,3))
print(i)
j = np.array([[2.5, 3.8, 1.5],
              [4.7, 2.9, 1.56]])
k = j.astype('int')
print(k)
l = np.array([[1, 0, 0],
              [1, 1, 1],
              [0, 0, 0]])
m = l.astype('bool')
print(m)
q = np.array([[1,2],
              [3,4],
              [5,6]])
r = np.array([[7,8],
              [9,10],
              [10,11]])
s = np.vstack((q, r))
print(s)
