print('\n=== Практические задания по множествам ===')
print('\n=== Задание №1 ===')
from random import random  # Подключение "рандомайзера"

# Задание №1
# Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
# Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.
list1 = []
list2 = []
n = 100  # определеим длинну будущих списков
for i in range(n):
    list1.append(int(random() * 1000))
for i in range(n):
    list2.append(int(random() * 1000))
set1 = set(list1)
set2 = set(list2)
# print(set1,'\n',set2) # Output for test or to see values in sets(lists)
print('Числа, которые входят как в первый, так и во второй список в порядке возрастания:\n',sorted(set1 & set2))
# print(*sorted(set1 & set2),sep=', ')  # output without []


print('\n=== Задание №2 ===')
# Задание №2
# Дан список чисел, который может содержать до 100000 чисел.
# Определите, сколько в нем встречается различных чисел.
list1 = []  # creating the list
n = 10000     # define the lenght of list
for i in range(n):
    list1.append(int(random() * 10000)) # filling the list
# print(list1)  #Output for testing
print('В случайно-сгенерированном списке находится',len(set(list1)),'различных(уникальных) значения.')
