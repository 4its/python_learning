from random import random       # importing randomizer
import array as arr             # importin arrays package(or module?!)

def arr_more_less_1(arr, b):
    i = 0
    while i < (len(arr)-1):
        if (arr[i] - arr[i+1]== b) | (arr[i] + arr[i+1]== b):
            print('Yes! Difference between',arr[i],'and',arr[i+1],'is',b)
            break
        i+=1
    else:
        print('NO! Our array does not contain two values in a row with a difference',b,'. Please, restart programm')

def arr_summ2prev(arr, b):
    i = 0
    while i < (len(arr)):
        if arr[i] == b:
            arr[i] = arr[i-1]+arr[i-2]
        i+=1
    print('Array after change',b,'values:',arr)

def arr_have_0(arr, b):
    i = 0
    while i < len(arr):
        if arr[i] == b:
            arr_summ2prev(arr, b)
            break
        i+=1
    else:
        print("Array doesn't contain",b,"values! Please, restart programm")

def arradd_byIndex(a, b, k):
    c = arr.array('i', )
    i = 0
    while i < len(a):
        c.append(a[i])
        if i == k-1:
            j = 0
            while j < len(b):
                c.append(b[j])
                j += 1
        i += 1
    return c

# functions for task #3
def arr_init(x=10):                 # fun for creating and fillin arr
    n = int(input('Enter length of array(must be int):'))
    a = arr.array('i',[int(random()* x) for i in range(n)])
    print('Defined array is:', a)
    return a

def arr_sum(a, b):
    if len(a)==len(b):
        i=0
        c = arr.array('i',)
        while i < len(a):
            c.append(a[i]+b[i])
            i+=1
        print('After summ elements in arrays A and B we have:', c)
    else:
        print('Arrays A and B have different length. Summ is imposible')

def arr_mult(a, b):
    i = 0
    while i < len(a):
        a[i] = a[i] * b
        i += 1
    print('After multiply elements by',b,'in array :',a)

def arr_common(a, b):
    c = list()
    if len(a) <= len(b):
        i = 0
        while i < len(a):
            j = 0
            while j < len(b):
                if a[i] == b[j]:
                    c.append(a[i])
                    break
                else:
                    j+=1
            i+=1
    else:
        i = 0
        while i < len(b):
            j = 0
            while j < len(a):
                if b[i] == a[j]:
                    c.append(b[i])
                    break
                else:
                    j += 1
            i += 1
    if len(c) != 0:
        print('List of common values for both arrays is',c)
    else:
        print("Presented array haven't common values. Please restart for another result")

def arr_valueprint(a):
    i=0
    print('Values in array is:',end=' ')
    while i < len(a):
        print(a[i],end=' ')
        i+=1

def arr_maxmin(a):
    max = 0
    min = (a[0]+1)*1000     # try to write in min bigger value
    i = 0
    while i < len(a):
        if a[i] > max:
            max = a[i]
        elif a[i]<min:
            min = a[i]
            i+=1
        else:
            i+=1
    print('In array min=',min,'and max=',max)

def arr_sorttomin(a):   #it is buble sort function
    swap = True
    while swap:
        swap = False
        i = 0
        while i < (len(a)-1):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swap = True
            i+=1
    print('Array after sorting is:',a)

print('Задачи для обязательного выполнения')
print('\n=== Task number #1 ===')
# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Вставить группу из M новых элементов, начиная с позиции K.
n = 10      # define array length
a = arr.array('i',[int(random()*10) for i in range(n)])     #creating and filling array
m = 5      # define count of new elements
k = 3       # define position where we want insert new values
print('We have an array:                                    ',a)
b = arr.array('i',[int(random()*10) for i in range(m)])     #creating and filling array that we want to add
print('Generated array of',m,'elements thas we want to insert:',b)
a=arradd_byIndex(a, b, k)
print('Our array after iserting another array in pos',k,'is:  ',a)

print('\n=== Task number #2===')
# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Поменять местами первую и вторую половины массива без использования
# дополнительных массивов
n = 10      # define array length
a = arr.array('i',[int(random()*10) for i in range(n)])     #creating and filling array
print('We have an array:      ',a)
i=0
while i < int(len(a)/2):
    a.append(a.pop(0))
    i+=1
print('Our array after change:',a)

print('\n=== Task number #3 ===')
# Реализовать проект – операций над массивами, каждая подзадача
# реализуется в виде отдельной функции:
print('\n=== Task number #3.1 инициализация массива ===')
# - инициализация массива с помощью датчика случайных чисел. Размер массива определяет пользователь
a = arr_init()

print('\n=== Task number #3.2 сложение массивов поэлементно ===')
# - сложение массивов поэлементно в случае равенства длины массивов
arr_sum(arr_init(),arr_init())

print('\n=== Task number #3.3 умножение массива на число поэлементно ===')
# - умножение массива на число осуществляется поэлементно
arr_mult(arr_init(),int(input('Enter multiplier for array(must be int):')))

print('\n=== Task number #3.4 поиск общих значений ===')
# - поиск общих значений двух массивов (длины массивов могут быть разные)
arr_common(arr_init(), arr_init())      # using additional value in function for more representative result

print('\n=== Task number #3.5 печать значений массива ===')
# - печать значений массива
arr_valueprint(arr_init())

print('\n=== Task number #3.6 упорядочивание значений массива по убыванию ===')
# # - упорядочивание значений массива по убыванию (без использования стандартных функций)
arr_sorttomin(arr_init())

print('\n=== Task number #3.7 поиск min, max значений в массиве ===')
# - поиск min, max значение в массиве, среднего значения всех значений массива (без использования стандартных функций)
arr_maxmin(arr_init())

print('\n\nЗадачи для самостоятельного выполнения')

print('\n=== Task number #4===')
# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Определить, имеются ли в массиве два подряд числа с разницей значений между ними 1.
n = 10      # define array length
b = 1       # choosed difference between values
# a = arr.array('i',[int(random()*10) for i in range(n)])     #creating and filling array
# print('We have an array:',a)
arr_more_less_1(arr_init(),b)

print('\n=== Task number #5===')
# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Вместо каждого элемента с нулевым значением поставить сумму двух предыдущих элементов массива.
n = 10      # define array length
b = 0       # define value that we want to find and replace
# a = arr.array('i',[int(random()*10) for i in range(n)])     #creating and filling array
# print('We have an array:           ',a)
arr_have_0(arr_init(),b)
