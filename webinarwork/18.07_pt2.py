import time
from random import random
from collections import deque
m = 50000000
# Standart list
# "for" cicle
start = time.time()
a = list()
for i in range(m):
    a.append(i)
#print(a)
end = time.time()
print(type(a))
print(end-start)
# by list comprehension
start = time.time()
b = [i for i in range(m)]
end = time.time()
print(type(a))
print(end-start)
print('Now lets use deque')
# Using deque
# "for" cicle
start = time.time()
c = deque()
for i in range(m):
    c.append(i)
#print(a)
end = time.time()
print(type(c))
print(end-start)
# by list comprehension
start = time.time()
d = deque([i for i in range(m)])
end = time.time()
print(type(d))
print(end-start)


