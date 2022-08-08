# def cylinder(h, r=1):  # В данном примере параметр r=1 - назначен по умолчанию.
#     side = 2 * 3.14 * r * h
#     circle = 3.14 * r ** 2
#     full = side + 2 * circle
#     print('First')
#     return full
#
# def cylinder(h, r = 1, x = 4):
#     side = 2 * 3.14 * r * h
#     circle = 3.14 * r ** 2
#     full = side + 2 * circle
#     print('Second')
#     return full
#
#
# figure1 = cylinder(4, 3)
# figure2 = cylinder(5)   # Благодаря параметру по умолчанию функция тоже будет работать!
# print(figure1)
# print(figure2)


# Slyde 56
# def call_with_five(function):   # Функция высшего порядка
#     return function(5)
#
# def add_one(x):
#     return x + 1
#
# def qqq(x):
#     return x * 10
#
# a = (call_with_five(add_one))
# print(a)
#
# a = (call_with_five(qqq))
# print(a)

# n = int(input())
# for i in range(1, n +1):
#     for j in range(1, n +1):
#         print(f"{j}х{i}={(i * j):2}", end=' ')

# s1 = 'торт'
# s2 = 'тортик'
# if s1 < s2:
#     print(s2)

# text = 'hello, my dear friends!'
# count = 0
#
# for letter in text:
#     if letter in 'aeiouy‘:
#         count += 1
# print(count)
#
# count = 0
# for i in range(len(text)):
#     if text[i] in 'aeiouy':
#        count += 1
# print(count)


# s = "0123456789"
# # del [3:9]
# s1 = s[:3] + s[9:]      # "0129"
# # insert string after 3rd symbol
# s2 = s[:3] + "ABC" + s[3:]  # "012ABC3456789"


# print('\u2603')

# text = 'hello, my dear friends!'
# count = 0
# for letter in text:
#     if letter in 'aeiouy':
#         count += 1
# print(count)


# Функция должна считать сумму чисел, но считает разность:
def sum(a, b):
    return a - b
# при таком вызове ошибка неочевидна, потому что
# и при сложении, и при вычитании будет один и тот же результат
print(sum(4, 0)) # 4
print(sum(4, 6))

if sum(2,3) == 5:
    print('All Ok')
else:
    print('Error')
