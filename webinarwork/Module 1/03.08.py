# # # def mul(a, b):
# # #     return a * b
# # #
# # # def mul5(a):
# # #     return mul(5, a)
# # #
# # # # print(mul(5, 4))
# # # # print(mul(5, 2))
# # #
# # # # print(mul5(4))
# # # # print(mul5(2))
# # #
# # # def mul1(a):
# # #     print('a=', a)
# # #     def helper(b):
# # #         print(' b=', b)
# # #         return a * b
# # #     return helper
# # #
# # # # print(mul1(5)(3))
# # #
# # # new_mul5 = mul1(5)
# # #
# # # print(new_mul5(2))
# #
# #
# # def fun1(a):
# #     x=a*3
# #     def fun2(b):
# #         # nonlocal x
# #         return b + x
# #     return fun2
# #
# #
# # test_fun = fun1(4)
# # print(test_fun(7))
#
#
# # def hi(name="yasoob"):
# #     def greet():
# #         return "Вы внутри функции greet()"
# #     def welcome():
# #         return "Вы внутри функции welcome()"
# #     if name == "yasoob":
# #         return greet
# #     else:
# #         return welcome
# #
# # a = hi()
# # print(a)
# # # Вывод: <function greet at 0x7f2143c01500>
# # print(a())
# # # Вывод: Вы внутри функции greet()
#
#
# # def hi():
# #     return "Привет yasoob!"
# #
# # def doSomethingBeforeHi(func):
# #     print("Я делаю что-то скучное перед исполнением hi()")
# #     print(func())
# #
# # doSomethingBeforeHi(hi)
#
# def decorator_function(wrapped_func):
#     def wrapper():
#         print('Выполняем обёрнутую функцию...')
#         wrapped_func()
#         print('Выходим из обёртки')
#     return wrapper
#
# def qqq(wrapped_func):
#     def wrapper():
#         print('Выполняем ВТОРУЮ обёрнутую функцию...')
#         wrapped_func()
#         print('Выходим из ВТОРОЙ обёртки')
#     return wrapper
#
#
# @decorator_function
# @qqq
# def hello_world():
#     print('Hello world!')
# hello_world()


# def param_transfer(fn):
#     def wrapper(arg):
#         print("Run function: " + str(fn.__name__) + "(), with param: " + str(arg))
#         fn(arg)
#     return wrapper
#
# @param_transfer
# def print_sqrt(num):
#     print(num**0.5)
#
# print_sqrt(4)

# def fact_rec(n):
#     print(n)
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact_rec(n - 1)
#
# print(fact_rec(5))




# def decor_with_return(fn):
#     def wrapper(*args, **kwargs):
#         print("Run method: " + str(fn.__name__))
#     return fn(*args, **kwargs) return wrapper


# def CalcSumNumbers(A):
#     if A == []:
#     # если набор пуст, возвратить 0
#         return 0
#     else:
#     # Вычислить сумму - прибавить первый элемент набора
#         summ = CalcSumNumbers(A[1:]) # рекурсивный вызов этой же функции # Прибавить к общей сумме первый элемент
#         summ = summ + A[0]
#     return summ
#
# # 1. Создать набор чисел
# L = [ 2, 3, 8, 11, 4, 6 ]
# # 2. Вызвать функцию
# summ = CalcSumNumbers(L)
# # 3. Распечатать сумму
# print("summ = ", summ)


def CalcSumNumbers(A):
    summ = 0                            # здесь нужно реализовать обход в цикле
    for t in A:                         # Обрабатывается элемент t
        if not isinstance(t, list):     # проверить, есть ли t списком
            summ = summ + t             # если t - не список, то прибавить его к сумме
        else:                           # получить сумму из следующих рекурсивных вызовов
            summ = summ + CalcSumNumbers(t)
    return summ
# 1. Создать набор чисел
L = [ -2, 3, 8, 11, [-4, 6, [ 2, [-5, 4] ] ] ]
# 2. Вызвать функцию
summ = CalcSumNumbers(L)
# 3. Распечатать сумму
print("summ = ", summ)





