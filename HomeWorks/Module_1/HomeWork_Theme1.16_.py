from array import array as arr
from random import random
from random import randrange
from collections import deque
from time import time


def bublesort(a):  # it is buble sort function
    swap = True
    while swap:
        swap = False
        i = 0
        while i in range(len(a) - 1):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swap = True
            i += 1
    return a
    # for i in range(st, end):        # This string need to see result of function
    #     print(a[i] )        # This string need to see result of function
    # print('\n')                     # This string need to see result of function


def insertionsort(a):
    for i in range(len(a)):
        lvi = i
        for j in range(i + 1, len(a)):
            if a[j] > a[lvi]:
                lvi = j
        a[i], a[lvi] = a[lvi], a[i]
    return a
    # for i in range(st, end):        # This string need to see result of function
    #     print(a[i] )                # This string need to see result of function
    # print('\n')                     # This string need to see result of function


def mergesort(a):
    if len(a) > 1:
        center = len(a) // 2
        left = a[:center]
        right = a[center:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
    return a
    # print(type(a))


def stack_list(from_, to):  # move data from stack to tmp list
    while len(from_) > 0:
        to.append(from_.pop())


print('=== Task 1 анализ времени работы каждого алгоритма ===')
# Дан массив вещественных чисел из 9000 элементов, формируемых с помощью датчика случайных чисел.
# Разбить массив на три части, отсортировать:
# 1 часть по убыванию методом пузырька,
# 2 часть – алгоритмом вставками,
# 3 часть – алгоритм слиянием.
# Выполнить сравнительный анализ времени работы каждого алгоритма сортировок.

start = time()
massiv = arr('f', [random() * 100 for i in range(9000)])  # array as array
# massiv = [random()*100 for i in range(9000)]        # array as list
arrtime = time() - start
print('Array created in                          ', arrtime, 'secends')
# print(massiv)

start = time()
bublesort(massiv[:3000])
bubletime = time() - start
print('Part of array sorted by bubble sort function in    ', bubletime, 'secends')

start = time()
insertionsort(massiv[3000:6000])
inserttime = time() - start
print('Part of array sorted by innsertion sort function in', inserttime, 'secends')

start = time()
mergesort(massiv[6000:])
mergetime = time() - start
print('Part of array sorted by merge sort function in     ', mergetime, 'secends')

massiv2 = []
start = time()
massiv2.append(bublesort(massiv[:3000]))
massiv2.append(insertionsort(massiv[3000:6000]))
massiv2.append(mergesort(massiv[6000:]))
endtime = time() - start
# print(massiv2)    # debuging string
print('Full time of programm(adding and sorting) is', endtime, 'seconds')
print('After all we can see that merge sort is preferred in that type of task.')

print('\n=== Task 2 имеются ли в массиве три подряд четных числа ===')
# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Определить, имеются ли в массиве три подряд четных числа.

n = int(input('Enter length of array: '))
massiv = arr('i', [int(random() * 100) for i in range(n)])
print(massiv)
flag = False
for i in range(len(massiv) - 2):
    if (massiv[i] % 2 == 0) and (massiv[i + 1] % 2 == 0) and (massiv[i + 2] % 2 == 0):
        flag = True
        # print(f'Yes! massiv[{i}] = {massiv[i]}, massiv[{i+1}] = {massiv[i+1]}, massiv[{i+2}] = {massiv[i+2]}')
if flag == False:
    print("No, we HAVEN'T a three even numbers in a row in our array")
else:
    print('Yes, we have a three even numbers in a row in our array')

print('\n=== Task 3 третий стек ===')
# Даны два стека случайных чисел, размеры стека не более 100 элементов.
# Выполнить объединение стеков в третий стек, располагая элементы в порядке убывания.
# Замечание: при выполнении данной задачи рекомендуется извлечь элементы первого стека и второго в общий массив,
# отсортировать данный массив, сформировать третий стек из полученного массива чисел.

coef = 100
stack1 = deque([int(random() * coef) for i in range(int(random() * coef))])
while len(stack1) == 0:  # Guarantee that length of stack will not be equal 0
    stack1 = deque([int(random() * coef) for i in range(int(random() * coef))])
stack2 = deque([int(random() * coef) for i in range(int(random() * coef))])
while len(stack2) == 0:  # Guarantee that length of stack will not be equal 0
    stack2 = deque([int(random() * coef) for i in range(int(random() * coef))])
stack3 = deque()  # Stack that we must fill
print('Stack1 is:', stack1, '\nStack2 is:', stack2)
listfromstacks = []  # temporary list
while len(stack1) > 0:  # Filling temp list from stacks
    listfromstacks.append(stack1.pop())
while len(stack2) > 0:  # Filling temp list from stacks
    listfromstacks.append(stack2.pop())
listfromstacks = mergesort(listfromstacks)  # sorting tmp list from low to high
stack_list(listfromstacks, stack3)  # filling stack3 from tmp list
print('\nStack3(from Stack1 and Stack2. Sorted) is: \n', stack3)

print('\n=== Task 4 планировщик очередей ===')
# Реализация планировщика очередей. Даны четыре очереди одинаковой длины.
# Значения очередей формируются на основе датчика случайных чисел, границы изменения значений 1-10.
# За один такт обработки очередей – обрабатывается один элемент очереди, который имеет наивысший приоритет -
# - максимальное значение из всех очередей.
# В случае равенства приоритетов обрабатывается очередь, которая имеет наибольшую длину.
# Напечатать порядок обслуживания очередей.

# queue1 = [4, 3, 2, 1]      # testing queue1
# queue2 = [5, 6, 7, 2]      # testing queue2
# queue3 = [8, 1, 4, 3]      # testing queue3
# queue4 = [2, 1, 5, 4]      # testing queue4

m = 10  # lenght of stacks

queue1 = [int(randrange(1, 11)) for i in range(m)]
queue2 = [int(randrange(1, 11)) for i in range(m)]
queue3 = [int(randrange(1, 11)) for i in range(m)]
queue4 = [int(randrange(1, 11)) for i in range(m)]

print("\nQueue 1 ", queue1)
print("Queue 2 ", queue2)
print("Queue 3 ", queue3)
print("Queue 4 ", queue4, '\n')
i = 0
n = len(queue1) + len(queue2) + len(queue3) + len(queue4)
while i < n:
    # print('Start', i, 'from', n)      # debuging comment
    tmp = []
    for item in queue1, queue2, queue3, queue4:
        if len(item) > 0:
            tmp.append(item[-1])
    try:
        mx = max(tmp)
    except ValueError:
        i += 1
        mx = 0
        continue
    count = tmp.count(mx)
    # print('Max is',mx,'and it count is =',count)  # debuging comment
    if count == 1:
        if len(queue1) > 0:
            if queue1[-1] == mx:
                print('number', queue1.pop(), 'Queue 1')
                mx, count = 0, 0
        if len(queue2) > 0:
            if queue2[-1] == mx:
                print('number', queue2.pop(), 'Queue 2')
                mx, count = 0, 0
        if len(queue3) > 0:
            if queue3[-1] == mx:
                print('number', queue3.pop(), 'Queue 3')
                mx, count = 0, 0
        if len(queue4) > 0:
            if queue4[-1] == mx:
                print('number', queue4.pop(), 'Queue 4')
                mx, count = 0, 0
    elif count > 1:
        if 0 < len(queue1) >= (len(queue2) & len(queue3) & len(queue4)):
            if queue1[-1] == mx:
                print('number', queue1.pop(), 'Queue 1')
                mx = 0
        if 0 < len(queue2) >= (len(queue1) & len(queue3) & len(queue4)):
            if queue2[-1] == mx:
                print('number', queue2.pop(), 'Queue 2')
                mx = 0
        if 0 < len(queue3) >= (len(queue1) & len(queue2) & len(queue4)):
            if queue3[-1] == mx:
                print('number', queue3.pop(), 'Queue 3')
                mx = 0
        if 0 < len(queue4) >= (len(queue1) & len(queue2) & len(queue3)):
            if queue4[-1] == mx:
                print('number', queue4.pop(), 'Queue 4')
                mx = 0
    i += 1
    # print("Queue 1 ", queue1)
    # print("Queue 2 ", queue2)
    # print("Queue 3 ", queue3)
    # print("Queue 4 ", queue4)
    # print('End',i,'from',n)   # debuging comment
print('\nEnd of all queues')
print("Queue 1 ", queue1)
print("Queue 2 ", queue2)
print("Queue 3 ", queue3)
print("Queue 4 ", queue4)
