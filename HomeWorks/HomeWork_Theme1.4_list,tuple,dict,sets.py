print('\n=== Практические задания по спискам ===')
from random import random  # Программа указала что для подключения "рандомайзера" нужно подключить генератор

print('=== Приступаем к заданию №1 ===')
# Задание 1 (стр 11)
# Допишите код, что бы вывести последний элемент списка.
# данный код
sample = ["abc", "xyz", "aba", 1221]
# требуемый вывод: 1221
print(sample[-1], '\n')  # выведем последний элемент через счет "справа на лево"
# print(sample[len(sample)-1])    #Альтернативный вариант вывода через индексы и встр.функ.
print('=== Переходим к заданию №2 ===')

# Задание 2 (стр 11)
# Допишите код, что бы вывести расширенный список
# данный код
sample = ["Green", "White", "Black"]
# требуемый вывод:
# ["Red", "Green", "White", "Black", "Pink", "Yellow"]
sample.insert(0, "Red")  # "вставим" с указанием индекса
sample.append('Pink')  # добавим в конец
sample.append('Yellow')  # добавим в конец
print(sample,
      '\n')  # Вывод правильный, но не уверен что правильно реализовал программу. Буду презнателен за комментарий.
print('=== Переходим к заданию №3 ===')

# Задание 3 (стр 12)
# Написать программу: дан список из 10 чисел, которые задаются с помощью датчика случайных чисел.
# Программа находит повторяющиеся элементы и считает количество повторений.
# Например дан список (1,1,1,2,3,4,2,3,4) результат
# число 1 повторяется 3 раза, число 2 – 2раза, число 3 - 2 раза, число 4 – 2 раза
n = 10
sample = []
for num in range(n):  # начинаем цикл для заполнения списка
    sample.append(int(random() * 100))  # ограничиваем рандомайзер целыми значениями в диапозоне от 0 до 9
print("С помощью датчика случайных чисел получаем следующий список:\n", sample)
for num in range(n):  # начинаем цикл для подсчета значений
    if sample.count(sample[num]) > 1:  # описываем условие, что если число не встречается, то и выводить не нужно.
        print('Число', sample[num], "встречается", sample.count(sample[num]), "раз(а)")
print('\n=== Переходим к заданию №4 ===')

# Задание 4 (стр 12)
# Написать программу: дан список из 10 чисел, которые задаются с помощью датчика случайных чисел.
# Программа находит повторяющиеся элементы и удаляет их из списка.
# Например дан список (1,1,1,2,3,4,2,3,4) результат (1,2,3,4)
n = 10
sample = []
for num in range(n):
    sample.append(int(random() * 10))
print("С помощью датчика случайных чисел получаем следующий список:\n", sample)
# Вариант решения 1 - перебор в лоб!
sample1 = sample[:]
sample1.reverse()  # Переверну массив чтоб было проще удалять дубликаты
i = len(sample1) - 1
while i >= 0:
    if sample1.count(sample1[i]) > 1:
        sample1.remove(sample1[i])
    i = i - 1
sample1.reverse()  # Вернем как было...
# Вариант решения 2
unique = []
for i in sample:
    if i in unique:
        continue
    else:
        unique.append(i)
# sample = unique[:] #этой записью мы перепишем основной список из временногого unique
print('Вывод решения №1:', sample1)
print("Вывод решения №2:", unique)
print('\n=== Переходим к заданию №5 ===')

# Задание 5 (стр 12)
# Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует,
# замените его на 200. Обновите список только при первом вхождении числа 20.
n = 10
sample = []
for num in range(n):
    sample.append(int(random() * 100))
print("С помощью датчика случайных чисел получаем следующий список:\n", sample)
# sample = [5, 10, 50, 20, 33, 77, 20]      #проверочный список для того чтоб не ждать генератор
i = 0
change = 0
while i < len(sample):
    if sample[i] == 20:
        sample[i] = 200
        change = 1
        break
    i += 1
if change == 1:  # условие для вывод в случае замены или без нее
    print("Список после изменения первого числа 20 в нём:\n", sample)
if change == 0:
    print("Числа 20 в представленном списке нет.\n(Перезапустите программу, возможно заполнится значение 20 в одну из ячеек списка)")
print('\n=== Переходим к заданию №6 ===')

# Задание 6 (стр 12)
# Поменять местами самый большой и самый маленький элементы списка
n = 10
sample = []
for num in range(n):
    sample.append(int(random() * 100))
print("С помощью датчика случайных чисел получаем следующий список:\n", sample)
# sample = [5, 10, 50, 20, 33, 77, 20]      #проверочный список для того чтоб не ждать генератор
imax = sample.index(max(sample))  # опеределеяем индекс МАКСИМАЛЬНОГО значения
imin = sample.index(min(sample))  # опеределеяем индекс МИНИМАЛЬНОГО значения
sample[imax], sample[imin] = sample[imin], sample[imax]  # меняем местами используя полученные ранее индексы
print('Список после обмена местами элементов \n', sample)

print('\n=== Практические задания по кортежам ===')
print('=== Приступаем к заданию №1 ===')
# Задание №1
# Создайте окртеж с цифрами от 0 до 9 и посчитайте сумму
# данный код numbers =
# print(sum(numbers))
# требуемый вывод: # 45
num_list = []  # Создади список
for num in range(10):  # Заполним список через цикл
    num_list.append(num)
numbers = tuple(num_list)  # преобразуем в кортеж
# print(numbers) #посмотрим на кортеж
print(sum(numbers))  # выведем результа
print('=== Переходим к заданию №2 ===')

# Задание №2
# Введите статистику частотности букв в кортеже.
# - решение 1 - использование циклов
# - решение 2 – использование встроенных функций
# данный код long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
# print("Количество 'т':", )
# print("Количество 'a':", )
# print("Количество 'и':", )
# требуемый вывод:
# Колличество 'т': 5
# Колличество 'а': 3
# Колличество 'и': 11
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
print(' Решение циклами:')
t_count = 0
a_count = 0
i_count = 0
for i in range(len(long_word)):
    if long_word[i] == 'т':
        t_count = t_count + 1
    elif long_word[i] == 'а':
        a_count = a_count + 1
    elif long_word[i] == 'и':
        i_count = i_count + 1
print("Количество 'т':", t_count)
print("Количество 'a':", a_count)
print("Количество 'и':", i_count)
print(' Решение встр.функциями:')
for i in set(long_word):
    print('Количество ',i ,':', long_word.count(i))

print('\n=== Практические задания по словарям ===')
print('=== Приступаем к заданию №1 ===')
# Задание №1
# Выведите значение возраста из словаря person
# данный код
person = {"name": "Kelly", "age": 25, "city": "New york"}
# требуемый вывод:
# 25
print(person.get('age'))
print('=== Приступаем к заданию №2 ===')

# Задание №2
# Значениями словаря могут быть и списки. Допишите словарь с ключами BMW, ВАЗ, Tesla
# и списками из 3х моделей в качестве значений.
# данный код
# models_data = {..., "Tesla": ["Modes S", ...]} print(models_data["Tesla"][0])
# требуемый вывод: Modes S
BMW = ["125", "325", "750i"]  # создаем список моделей
VAZ = ["2101", "2106", "2109"]  # создаем список моделей
TESLA = ["Model S", "Model Y", "Model X"]  # создаем список моделей
KIA = ["Rio", "CEED", "Sportage"]  # создаем список моделей
models_data = {"BMW": BMW, "ВАЗ": VAZ, "Tesla": TESLA, "KIA": KIA}  # создаем словарь используя списки моделей авто
print(models_data["Tesla"][0])
print('\n=== Приступаем к заданию №3 ===')
del models_data

# Задание №3
# Дан список из 10 чисел, которые задаются случайном образом.
# Сформировать словарь по следующему принципу: ключ (one, two, three):элемент
# списка models_data = {“one”:1, “two”:2, “tree”:2, “four”:3...}
# Задача подсчитать количество повторений значений. Пример значение 2 – встречается дважды.
n = 10
keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
values = []
for num in range(n):
    values.append(int(random() * 100))
print('Получаем список из ', n, ' чисел:', values)
models_data = {}
for num in range(n):
    models_data.setdefault(keys[num], values[num])
print("Получаем словарь: ", models_data)
if len(values) == len(list(set(values))):
    print("Повторяющихся значений нет. Перезапустите программу и Вам повезёт!")
for i in list(set(values)):
    if values.count(i) > 1:
        print('Значение', i, "встречается -", values.count(i), 'раз(а).')
print('\n=== Приступаем к заданию №4 ===')

# Задание №4
# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.
list1 = []
list2 = []
n = 15  # определеим длинну будущих списков
for i in range(n):
    list1.append(int(random() * 100))
print('Получаем список #1 длинной ', n, ':', list1)
for i in range(n):
    list2.append(int(random() * 100))
print('Получаем список #2 длинной ', n, ':', list2)
dict1 = {}
for i in range(n):
    dict1.setdefault(list1[i], list2[i])
print("Выводим словарь из списков 1 и 2:", dict1)
print('\n=== Приступаем к заданию №5 ===')

# Задание №5
# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
list1 = []
list2 = []
n = 5  # определеим длинну будущих списков
for i in range(n):
    list1.append(int(random() * 100))
for i in range(n):
    list2.append(int(random() * 100))
dict1 = {}
for i in range(n):
    dict1.setdefault(list1[i], list2[i])
print('У нас есть словарь(сгенерир.сл.образом):', dict1)
mult = 1  # начальный множитель
for key in dict1.keys():  # итерируем ключи словаря
    mult = mult * dict1.get(key)  # умножаем на занчение ключа key
print('Результат перемножения значений словаря =', mult)
print('\n=== Приступаем к заданию №6 ===')

# Задание №6
# Создайте словарь из строки 'pythonist' следующим образом: в качестве ключей возьмите буквы строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
str_p = 'pythonist'
dict1 = {}
for i in range(len(str_p)):
    dict1.setdefault(str_p[i], str_p.count(str_p[i]))
print('От нас хотели получить словарь следующего содержания:\n', dict1)

print('\n=== Практические задания по множествам ===')

print('\n=== Задание №1 ===')
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
print('Числа, которые входят как в первый, так и во второй список в порядке возрастания:\n', sorted(set1 & set2))
# print(*sorted(set1 & set2),sep=', ')  # output without []


print('\n=== Задание №2 ===')
# Задание №2
# Дан список чисел, который может содержать до 100000 чисел.
# Определите, сколько в нем встречается различных чисел.
list1 = []  # creating the list
n = 10000  # define the lenght of list
for i in range(n):
    list1.append(int(random() * 10000))  # filling the list
# print(list1)  #Output for testing
print('В случайно-сгенерированном списке находится', len(set(list1)), 'различных(уникальных) значения.')
