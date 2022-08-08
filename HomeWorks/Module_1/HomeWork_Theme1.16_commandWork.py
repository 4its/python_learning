
from array import array # import array
from random import random

def create_random(n = 10):
    arr = [int(random()*100) for i in range(n)]
    return arr

def create_manual(n = 10):
    arr = []
    for i in range(n):
        a = 'Enter element '+ str(i+1)+' from '+str(n)+': '
        arr.append(int(input(a)))
    return arr

def create_from_file(file, n = 10):
    try:
        fo = open(file, 'r')
    except FileNotFoundError:
        nums_arr = str()
        for i in range(n):
            nums_arr = nums_arr + str(int(random()*100))+' '
        fo = open(file, 'w')
        fo.write(nums_arr)
    arr = list(fo.read().split())
    print(arr)
    fo.close()
    for element in arr:
        element = int(element)
    print(arr)
    return arr

def printarray(array):
    print('Elements in array is:',*array)

def find_value(arr, fv):
    fva = []
    for i,j in enumerate(arr):
        if j == fv:
            fva.append(i)
    if len(fva) > 0:
        print('Indexes of number', fv,'in array is:',*fva)
    else:
        print('No indexes of',fv ,'in array' )

def delete_value(arr, fv):
    i = 0
    while i < len(arr):
        if arr[i] == fv:
            arr.pop(i)
        i+=1
    return arr

def average(arr):
    sum = 0
    for i in arr:
        sum = sum + int(i)
    return sum / len(arr)

def summ_arrays(arr1, arr2):
    if len(arr1) == len(arr2):
        arr3 = []
        for i in range(len(arr1)):
            arr3.append(arr1[i]+arr2[i])
        return arr3

    else:
        print("Arrays length isn't equal. Can's sum arrays with different length")

# sample = array('i',[10, 50, 20, 30, 40 ,50 ,60, 70, 50])

sample = create_from_file('test.txt', 10)

printarray(sample)

find_value(sample, 75)

print(*delete_value(sample, 50))