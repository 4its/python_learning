from array import array as arr
from random import random


def create_random(n = int(random()*100)):
    return arr('i',[int(random()*100) for i in range(n)])

def create_manual(a):
    a = arr('i')
    n = int(input('Etnter length of array: '))
    for i in range(n):
        b = int(input('Enter element of array: '))
        a.append(b)
    return a

def print_array(array):
    n = len(array)
    print('Numbers in array: ')
    for item in array:
        print(item)


massiv = ('i', [33, 47, 73, 60, 21, 75, 46, 93, 13, 79])    # study array
print(massiv)

for a in massiv:
    print(a)

for b in range(0, len(massiv)):
    print(f'massiv[{b}] = {massiv[b]}')






# B = [x for x in b if x % 2 == 0]
# print(sum(B))
