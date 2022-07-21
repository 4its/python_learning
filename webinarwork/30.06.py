# Занятие по Циклам
# spisok = [10,40,20,30]
# i=0
#var 1
#for element in spisok:
#    spisok[i]=element+2
#    i=-1
#print(spisok)
#var 2
# for i in range(len(spisok)):
#     spisok[i]+=2
# print(spisok)

# пример Встроенной функции
# print(ord("z"))
# print(chr(122))

# function MAP
base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]
# numbers_powers = list(map(pow, base_numbers, powers))
# print(numbers_powers)
# i=0
# for element in base_numbers:
#    base_numbers[i] = pow(base_numbers[i],i)
#    i+=1
# print(base_numbers)

# Встроенная функция zip
# emloyee_numbers = (2,9,18,28)
# employee_names = ("Дима","Марина","Андрей","Никита")
# zipped_values = zip(employee_names, emloyee_numbers)
# zipped_list = list(zipped_values)
# print(zipped_list)


# def countFood():
#     a = int(input())
#     b = int(input())
#     print("Всего", a+b, "шт.")
# print("Сколько огурцов и помидор купить?")
# countFood()
# print("Сколько яблок и груш купить?")
# countFood()


# Пример функций
def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    print("Площадь: %.2f" % (a * b))

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print("Площадь: %.2f" % (0.5 * a * h))

def circle():
    r = float(input("–Радиус: "))
    print("Площадь: %.2f" % (3.14 * r ** 2))

figure = input("1-прямоугольник,2 - треугольник, 3 - круг: ")
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
elif figure == '3':
    circle()
else:
    print("Ошибка ввода")

# print("Пример: локальная переменная")
# def f():
#     #локальныя переменная х
#     x = 100
#     print(x)
#
#
# f()
#prinx(x) - вызов локальной переменной в главной программе приведет к ошибке компилятора
# print("Пример: глобальная переменная")
# x = 100 #глобальная переменная
# def f():
#     x = 101 #локальная переменная
#     print(x)
# print("before ", x)
# f()
# print("after ", x)
# print("Пример: глобальная переменная 2")
# x = 100 #глобальная переменная
# def f():
#     global x # подскажем, что  х - глобальная переменная
#     x = 101 #локальная переменная
#     print(x)
# print("before ", x)
# f()
# print("after ", x)
#
# a=0
# b=0
#
# def summa():
#     global a
#     global b
#     print("Всего: ",a+b), "шт."
#
# def mult():
#     global a
#     global b
#     print("Всего: ",a*b), "шт."
#
# a = int(input())
# b = int(input())
# summa()
# mult()

# Программа 3

# def cylinder():
#     r = float(input())
#     h = float(input())
#     # площадь боковой поверхности цилиндра:
#     side = 2 * 3.14 * r * h
#     # площадь одного основания цилиндра:
#     circle = 3.14 * r**2
#     # полная площадь цилиндра:
#     full = side + 2 * circle
#     v = 3.14 * r * r * h
#     return full, v
# square,volume = cylinder()
# #print(cylinder()) #Так тоже будет работать!
# print(square, volume)

# страница 30-31 ДЗ