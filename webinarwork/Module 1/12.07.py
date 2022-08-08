# import packages
# print(packages.NAME)


# # Вызовы из пакета:
# # Вариант 1
# import packages.functions
# import packages.constants
# packages.functions.greet(packages.constants.PERSON)
# # Вариант 2
# from packages.functions import greet
# from packages.constants import PERSON
# greet(PERSON)
# # Вариант 3
# import packages.functions as pf
# import packages.constants as pc
# pf.greet(pc.PERSON)

# packages.functions.greet(packages.constants.PERSON)

import numpy as np
# # a = np.array([1, 2, 3])
# # print(a)
# a = np.array([2, 3])
# b = np.array([4, 5])
# c = a + b
# print(a)
# print(b)
# print('c\n', c)
#
# a = np.array([2, 3, 4, 5, 6, 7, 8])
# print(a)
# # b = a
# b = a[2:5]  # В данном случае срез передается по ССЫЛКЕ!!!!
# print('b before change\n', b)
# b[1] = 99
#
# print('a \n',a)
# print('b \n',b)


# a = np.array([2, 3, 4, 5, 6, 7, 8])
# b = np.array([9, 10, 11])

# import array as arr
# numbers = arr.array('i',[10,20,30])
# print('before changes = ', numbers)
# #numbers[0] = 99.6
# numbers[0] = int(99.6)
# print(numbers)
# print(numbers[-1])

import array as arr
# numbers = arr.array('d',[10,20,30, 40, 50, 99])
# print('before changes = ', numbers)
# #numbers[0] = 99.6
# numbers[0] = int(99.6)
# print(numbers)
# print(numbers[-1])


a = arr.array('d',[10,20,30, 40, 50, 99])
print('a=',a)
b = a[0:6]
print('b=',b)
b[1] = 99

print('a=',a)
print('b=',b)