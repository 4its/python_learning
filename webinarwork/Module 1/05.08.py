# def summa(a, b):
#     return a+b
# print('summa=', summa(5,4))
#
#
# add = lambda x,y:x+y
# print(add(5,4))

# def make_adder(n):
#     return lambda x: x + n
#
# plus_3 = make_adder(3)
# plus_5 = make_adder(5)
#
# print("4 ",plus_3(4))
# print("4 ",plus_3(4))
# print("5 ",plus_3(4))
# print("6 ",plus_3(4))
# print("7 ",plus_3(4))

# def apply_discount(product, discount):
#     price = int(product['цена'] * (1.0 - discount))
#     assert 0 <= price <= product['цена']
#     return price
#
# shoes = {'имя': 'Модные туфли', 'цена': 14900}
# # print( apply_discount(shoes, 0.25) )
# print( apply_discount(shoes, 2.0) )

# x = [True, True, False]
# if any(x):
#     print("Как минимум один True")
# if all(x):
#     print("Ни одного False")
# if any(x) and not all(x):
#     print("Как минимум один True и один False")

# dictionary = {"a": 1, "b": 2}
# def some_function(a, b):
#     print(a + b)
#     return
# # оба варианта делают одно и то же:
# some_function(**dictionary)
# some_function(a=1, b=2)

# numbers = [1, 2, 3, 4, 5, 6, 7]
# evens = [x for x in numbers if x % 2 == 0]
# odds = [y for y in numbers if y not in evens]
# print(evens, '\n', odds)
# cities = ['Лондон', 'Москва', 'Берлин']
# def visit(city):
#     print("Добро пожаловать в", city)
# for city in cities:
#     visit(city)


# keys = ['a', 'b', 'c']
# vals = [1, 2, 3]
# zipped = dict(zip(keys, vals))
# print(zipped)

L = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print(sum(L, []))
