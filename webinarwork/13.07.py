import array as arr

# numbers = arr.array('i',[10,20,30])
# print('before: ',numbers)
# print(numbers[:2])
# numbers.append(40) добавление
# numbers.extend([40, 50, 60]) # добавление нескольких значений
# numbers.insert(0, 40) # вставка в конкретное место
# numbers.pop(1) # удаление значения по индексу
# print(numbers.count(20)) #counter
# print(numbers)

# из списка в массив
# r = [11, 12, 13]
# t = arr.array('i', r)
# print(t)

import collections
# list_of_letters = list('абракадабра')
# letter_cnt = collections.Counter(list_of_letters)
# print(letter_cnt)
# # print(letter_cnt['ю']) # вернет 0, а не ошибку!
# # print(letter_cnt)
# letter_cnt['ю'] = 3
# letter_cnt['н'] = 3
# letter_cnt['ю'] = 7 # перезапишет предедущее значение "3"
# print(letter_cnt)
# # del letter_cnt['ю']
# print(letter_cnt)
#
# emotion_cnt = collections.Counter() # write it
# print(letter_cnt.most_common(3))


# list_of_letters1 = list('абракадабра')
# letter_cnt1 = collections.Counter(list_of_letters1)
# print(letter_cnt1)
# list_of_letters2 = list('приветкакделаинастроение')
# letter_cnt2 = collections.Counter(list_of_letters2)
# print(letter_cnt2)
# print(letter_cnt1+letter_cnt2)
# print(letter_cnt1-letter_cnt2)


# d = collections.defaultdict(str)
# d['name'] = 'James'
# d['surname'] = 'Bond'
# print(d['patronomic'])
#
# print(d)
# d['patronomic'] = 'Viktorovich'
# print(d)


# dict_of_list = collections.defaultdict(list)
# for i in range(5):
#     dict_of_list[i].append(i)
# print(dict_of_list)
# dict_of_list[0] = [10,20,30]
# print(dict_of_list)

# d = collections.OrderedDict.fromkeys('abcde')
# print('before: ',d)
# d.move_to_end('b')
# print('after change 1:',d)
# d.move_to_end('b', last=False)#.join(d.keys())
# print('after change 2:',d)

# letters = {'a': 1, 'b': 2}
# vowels = {'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5}
# chain = collections.ChainMap(letters, vowels)
# print(chain)
# print(chain['b'])
# letters['c'] = 3
# print(chain)
#
# consons = {'a':3, 'b':2, 'c': 1}
# # дописать

# seq = list('bcd')
# deq = collections.deque(seq)
# print('before change: ',deq)
# deq.append('e')     #add to end
# # deq.pop()  тоже работает
# print('after change 1: ',deq)
# deq.appendleft('a') # добавление в начало(левый конец)
# # deq.popleft()  тоже работает
# print('after change 2: ',deq)


# n = input("Введите целое число: ")
# try:
#     n = int(n)
#     print("Удачно")
# except:
#     print("Что-то пошло не так")


# try:
#     n = input("Введите целое число: ")
#     n = int(n)
#     print("Все верно, вы ввели число: ",n)
# except ValueError:
#     print("Вы ввели не целое число")

try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    c = a / b
    print("Частное: %.2f" % c)
except ValueError:
    print("Нельзя вводить строки")
except ZeroDivisionError:
    print("Нельзя делить на ноль")
except:
    print("Что-то пошло не так...")
