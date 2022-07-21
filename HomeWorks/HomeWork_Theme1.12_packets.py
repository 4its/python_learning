import numpy
import workwithnums as wn       #importing module workwithnums as wn

from figure import *    # importing all features from figure package
# Notice - you can UNCOMMENT strings below and you will see that they works too! (Dont' forget to commnet string # 4)
# from figure import square_area
# from figure import square_perimeter
# from figure import triangle_area
# from figure import triangle_perimeter
# from figure import triangle_define


print('\n=== Tesk 1 ===')
a = int(input('Please, enter number a: '))
b = int(input('Please, enter number b: '))
# even od odd
wn.even_odd(a, b)
# find max
wn.max_min(a, b)
# find who can be divisioned by 5
wn.division5(a, b)
# find summ of a and b
wn.summ(a, b)
# find squared a and b
wn.sqr(a, b)

print('\n=== Tesk 2 and 3 by third scenario ===')
print('Enter triangle sides length')
try:            # lets use error exception for using default data when entered wrong data
    a = int(input("Side 1 length is: "))        # entering side
    b = int(input("Side 2 length is: "))        # entering side
    c = int(input("Side 3 length is: "))        # entering side
    print("You entered: ",a,b,c)                # displaying entered values
    print('Triangle perimeter with entered sizes length is:',triangle_perimeter(a, b, c))    # using func from package
    print('Triangle area with entered sizes length is:', triangle_area(a, b, c))             # using func from package
    triangle_define(a, b, c)        # using func from package
except ValueError:
    print("ERROR: Incorrect input. Lets use default values")
    print('Triangle perimeter with default sizes length is:', triangle_perimeter()) # using func from package with default value
    print('Triangle area with default sizes length is:', triangle_area())           # using func from package with default value
    triangle_define()

print('\nEnter square side length')
try:            # lets use error exception for using default data when entered wrong data
    a = int(input("Side length is: "))      # entering side
    print("You entered: ",a)                # displaying entered values
    print('Square perimeter with entered sizes length is:',square_perimeter(a))  # using func from package
    print('Square area with entered sizes length is:', square_area(a))           # using func from package
except ValueError:
    print("ERROR: Incorrect input. Lets use default values")
    print('Square perimeter with default sizes length is:', square_perimeter()) # using func from package with default value
    print('Square area with default sizes length is:', square_area())           # using func from package with default value


print('\n=== Task 4 ===')
# Решите без использования циклов средствами NumPy (каждый пункт решается в 1-2 строчки)
# Создайте вектор с элементами от 12 до 42
print(numpy.arange(12,43))
# Создайте вектор из нулей длины 12, но его пятый элемент должен быть равен 1
vek = numpy.zeros(12)
vek[4] =1
print('\n',vek)
# Создайте матрицу (3, 3), заполненную от 0 до 8
print('\n',numpy.arange(9).reshape(3,3))
# Найдите все положительные числа в np.array([1,2,0,0,4,0])
# Умножьте матрицу размерности (5, 3) на (3, 2)
a, b = numpy.random.random((5, 3)), numpy.random.random((3, 2))
print('\n',numpy.dot(a, b))
# Создайте матрицу (10, 10) так, чтобы на границе были 0, а внутри 1
arr = numpy.ones((10, 10))
arr[1:-1, 1:-1] = 0
print('\n',arr)