from random import random  # Программа указала что для подключения "рандомайзера" нужно подключить генератор
print('=== Практическое задание по теме Функции ===\n')

print('=== Задание №1 ===')
# Задание №1
# Написать программу, которая последовательно вызывает три функции.
# Функция 1 – подсчитывает для заданного отрезка чисел все числа, которые делятся нацело на 3
# Функция 2 – подсчитывает для заданного отрезка чисел все числа, которые делятся нацело на 4
# Функция 3 – подсчитывает для заданного отрезка чисел все числа, которые делятся нацело на 5

def func1(int1, int2, int3):            #Данной функцией реализуем все 3 решения
    for num in range(int1, int2+1):     #добавили +1 чтобы указанное число входило в границу
        if num % int3 == 0:
            lst.append(num)
    print('Список чисел на отрезке от', int1, 'до', int2, 'которые делятся нацело на', int3, ':',lst)

lst = []
a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец  отрезка: '))
for i in range(3, 6):   # Выполним нашу функцию с известным заданным кратным
    func1(a, b, i)
    lst = []            # очистка списка после каждой итерации

print('\n=== Задание №2 ===')
# Задание №2
# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода.
# Это вызов функции test(). В ней запрашивается на ввод целое число. Если оно положительное,
# то вызывается функция positive(), тело которой содержит команду вывода на экран слова "Положительное".
# Если число отрицательное, то вызывается функция negative(),
# ее тело содержит выражение вывода на экран слова "Отрицательное".

def positive():
    print('Положительное')
def negative():
    print('Отрицательное')
def test():
    if int(input("Введите число: "))>=0:
        positive()
    else:
        negative()
test()

print('\n=== Задание №3 ===')
# Задание №3
# Дано натуральное число 𝑥>1. Проверьте, является ли оно простым.
# Программа должна вывести слово YES, если число простое и NO, если число составное

def simple(int1):
    k=0
    for num in range(2, int1 // 2 + 1):
        if (int1 % num == 0):
            k = k + 1
    if (k <= 0):
        print("YES")
    else:
        print("NO")
a = int(input("Введите число: "))
simple(a)

print('\n=== Задание №4 ===')
# # Задание №4
# # Выполнить циклический сдвиг в списке целых чисел на указанное число шагов.
# # Сдвиг также должен быть кольцевым, то есть элемент, вышедший за пределы списка,
# # должен появляться с другого его конца.
def circle_shift(lst, step):
    if step >= 0:
        for i in range(step):
            lst.insert(0, lst.pop())
    else:
        step = abs(step)
        for i in range(step):
            lst.append(lst.pop(0))
lst = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
print('Before: ',lst)
st = int(input('Введите шаг сдвига: '))
circle_shift(lst, st)
print('After:  ',lst)

print('\n=== Задание №5 ===')
# Даны два действительных числа 𝑥 и 𝑦. Проверьте, принадлежит ли точка с координатами (𝑥,𝑦) заштрихованному
# квадрату (включая его границу). Если точка принадлежит квадрату, выведите слово YES, иначе выведите слово NO.
# На рисунке сетка проведена с шагом 1.

def inSqr(x, y):
    if -1 <=x and x<=1:
        if -1 <= y and y <= 1:
            print("YES")
        else:
            print('NO')
    else:
        print('NO')
x = float(input('Введите координату х: '))
y = float(input('Введите координату y: '))
inSqr(x, y)

print('\n=== Задание №6 ===')
# В основной ветке программы вызывается функция cylinder(), которая вычисляет площадь цилиндра.
# В теле cylinder определена функция circle, вычисляющая площадь круга по формуле πr2.
# В теле cylinder у пользователя спрашивается, хочет ли он получить только площадь боковой поверхности цилиндра,
# которая вычисляется по формуле 2πrh, или полную площадь цилиндра.
# В последнем случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат вычислений
# функции circle().

def cylinder():
    pi = 3.1415
    r = float(input('Введите радиус окружности: '))
    h = float(input('Введите высоту целиндра: '))
    S_circle = 0
    def circle():
        global S_circle
        S_circle = pi * pow(r, 2)
    print('Выберите, что будем считать:')
    print('1 - только площадь боковой поверхности')
    print('2 - полную площадь цилиндра')
    ans = int(input('Напишите номер варианта ответа: '))
    S_cylinder = 2 * pi * r * h
    if ans == 1:
        print('Площадь боковой поверхности:',S_cylinder)
    elif ans == 2:
        circle()
        S_full_cyl = S_cylinder + 2*S_circle
        print('Полная площадь цилиндра ',S_full_cyl)
    else:
        print("Введено неверное заначение...")
cylinder()

print('\n=== Задание №7 ===')
# Задание 7
# Дан список целых чисел. Посчитать, сколько раз в нем встречается каждое число.
# Например, если дан список [1, 1, 3, 2, 1, 3, 4], то в нем число 1 встречается три раза,
# число 3 - два раза, числа 2 и 4 - по одному разу.

def fill(list, count):             #filling list function
    for num in range(count):
        list.append(int(random() * 10))
def task7(num):
    print('Число',num,'встречается',lst.count(num),'раз')

lst = []        # defining list
n = 10          # defining list lenght
fill(lst,n)     # filling the list
print('Имеем случайный список: ',lst)
for num in set(lst):        #getting cycle to get answer
    task7(num)

print('\n=== Задание №8 ===')
print('Это задание полностью дублирует Задание №4')

print('\n=== Задание №9 ===')
# Задание 9.
# Даны два списка целых чисел одинаковый длины. Например [5,4,3] и [2,1,3].
# Сформировать третий список полученный путем нахождения разницы меду списками, например [5-2, 4-1,3-3]
# итоговый список [3,3,0]. Формирование третьего списка осуществляется с использованием функции.

def razn(a, b, lenght):
    razn_lst = []
    for num in range(lenght):
        razn_lst.append(a[num]-b[num])
    return razn_lst
n = 3                           #defining list lenght
lst1, lst2 = [], []             #creating lists
fill(lst1, n), fill(lst2, n)    #filling lists
print('Список №1', lst1,'\nСписок №2', lst2,)
print('3-й список:',razn(lst1, lst2, len(lst1)))