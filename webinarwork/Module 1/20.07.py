from time import time
#
#
# my_items = ['a', 'b', 'c']
# one = []
# t = time()
# for j in range(1000000):
#     i = 0
#     while i < len(my_items):
#         one.append(my_items[i])
#         #print(my_items[i])
#         i+=1
# print("total run time:")
# print(time()-t)
#
# t = time()
# for j in range(1000000):
#     for i in range( len(my_items)):
#         one.append(my_items[i])
#         #print(my_items[i])
# print("total run time:")
# print(time()-t)
#
# t = time()
# for j in range(1000000):
#     for item in my_items:
#         one.append(item)
#         #print(my_items[i])
# print("total run time:")
# print(time()-t)
#
# t = time()
# for j in range(1000000):
#     for i,item in enumerate(my_items):
#         #print(f'{i}: {item}')
#         one.append(item)
# print("total run time:")
# print(time()-t)

# import numpy as np
# # range for floats with np.arange()
# for i in np.arange(0, 4.5, 0.5):
#     print(i, end=', ')
#
# print('\n-----')
# # Output 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, # Example 2
# for i in np.arange(5.5, 15.5, 2.5):
#     print(i, end=' ')
# # Output 5.5, 8.0, 10.5, 13.0

# a = ['foo', 'bar']
# while len(a):
#     print(a.pop(0))
#     b = ['baz', 'qux']
#     while len(b):
#         print('>', b.pop(0))
# print('')


# n= 5
# while n > 0: n -= 1; print(n)

# i = 100
# j = 200
# while i < 105:
#     while j < 205:
#         if j == 203:
#             i+=1
#             break
#         print('J', j)
#         j += 1
# print('I', i)
# i += 1

# n = int(input())
# m = int(input())
# for i in range(n):
#     for j in range(m):
#         print('*', end='')
#     print()

# k = int(input())
# for i in range(1, 10):
#     print(i, '*', k, '=', k * i, sep='', end='\t')

# A = [ [1, 2, 3], [4, 5, 6] ]
#
# for row in A:
#     for elem in row:
#         print(elem, end = ' ')
#     print()
# print('\n')
# for row in A:
#     print(' '.join(map(str, row)))
# print('\n')

# m,n = 4,3
# A = [[0] * m] * n
#
# for row in A:
#     for elem in row:
#         print(elem, end = ' ')
#     print()
# print(A)

# A = [[0] * m for i in range(n)]
# print(A)

# m,n = 10,10
# A = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]
#
# for row in A:
#     for elem in row:
#         print(elem, end = ' ')
#     print()



list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]
for a in list_a:
    for b in list_b:
        for c in list_c:
            if a + b + c == 2077:
                print(a, b, c)

from itertools import product
list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]
for a, b, c in product(list_a, list_b, list_c):
    if a + b + c == 2077:
        print(a, b, c)


from itertools import chain
list_a = [1, 22]
list_b = [7, 20]
list_c = [3, 70]
for i in chain(list_a, list_b, list_c):
    print(i)

def even_only(num):
    for i in num:
        if i % 2 == 0:
            yield i
my_list = [1, 9, 3, 4, 2, 5]

for n in even_only(my_list):
    print(n)

#4
#2



