from random import randint as rnd

print('=== Task #1 класс – прямоугольник ===')
# Написать класс – прямоугольник. Учитывая следующие рекомендации:
# - создайте метод __init__(), внутри которого будут определены два динамических свойства:
#   ширина, длина. Начальные значения свойств берутся из входных параметров метода.
# -	создайте метод print() – вывод на экран параметров прямоугольника – ширина-высота,
# -	создайте метод PrintP  - который возвращает периметр прямоугольника
# -	создайте метод PrintS  - который возвращает площадь прямоугольника
# -	создайте метод __eq__(self, other) сравнивает два прямоугольника на основании площади, выводит на экран результат сравнения

class Rectangle:

    def __init__(self, w, l):
        self.width, self.length = w, l

    def prnt(self):         # создайте метод print() – вывод на экран параметров прямоугольника – ширина-высота
        print('Width is:', self.width)
        print('Length is:', self.length)

    def prntP(self):
        return (self.width + self.length) * 2

    def prntS(self):
        return (self.width * self.length)

    def __eq__(self, other):
        if self.prntS() == other.prntS():
            print('Rectangles have same area')
        else:
            print('Different area of rectangles')


rect_a = Rectangle(3, 5)        # rectangle #1
rect_b = Rectangle(3, 5)        # rectangle #2

print("Call method print()")
rect_a.prnt()
print("\nCall method for perimetr =>")
print('Perimetr of rectangle is:', rect_a.prntP() )
print("\nCall method area =>")
print('Rectangle area is:',rect_a.prntS())
print("\nCall method __eq__ =>")
rect_a == rect_b

print('\n=== Task #2 класс – списки целых чисел ===')

# Написать класс – списки целых чисел. Учитывая следующие рекомендации:
# - создайте метод __init__(), внутри которого будут определен один параметр: размер списка.
#           Начальные значения свойства берутся из входных параметров метода.
# -	создайте метод InputData позволяющий задать данные списка пользователем
# -	создайте метод InputDataRandom заполняющий список с помощью датчика случайных чисел
# -	создайте метод print() – вывод на экран содержимого списка
# -	создайте метод FindValue  - который возвращает список индексов для искомого элемента
# -	создайте метод DelValue  - который удаляет из списка искомый элемент.
# -	создайте метод FindMax- который возвращает максимальное значение из списка.
# -	создайте метод __add__(self, other) который выполняет сложение двух списков одинаковой длина поэлементно

class IntList:

    a,b = 0, 10        # define area for random generator set
    inlst = []
    def __init__(self, n):      # init with defining length of list
        self.n = n

    def prnt(self):             # метод print()
        if len(self.inlst) == 0:
            print('List is empty, please fill it if you want to see some values')
        else:
            print('Our list is:', self.inlst)

    def InputData(self):        # метод InputData
        self.inlst = [(int(input('Enter the element of list(int only):'))) for i in range(self.n)]

    def InputDataRandom(self):  # метод InputDataRandom
        self.inlst = [rnd(self.a, self.b) for i in range(self.n)]

    def FindValue(self, fv):    # метод FindValue
        tmp = [i for i,item in enumerate(self.inlst) if item == fv]

        if len(tmp) == 0:       # Checking list that it not empty
            print("There is no value", fv, "in list.")
        else:
            print('Found value', fv, 'in next indexes:', tmp)

    def DelOneValue(self, fv):      # метод DelValue (will delete first entered value)
        if fv in self.inlst:
            self.inlst.remove(fv)
            # print('List after delete FIRST',fv , 'value:', self.inlst)     # Debugging print
        else:
            print('Value', fv, 'not in list.')

    def DelAllValues(self, fv):     # метод DelValue (will delete ALL entered value)
        if fv in self.inlst:
            tmp = [i for i, item in enumerate(self.inlst) if item == fv]
            for item in reversed(tmp):
                self.inlst.pop(item)
        else:
            print('Value', fv, 'not in list.')

    def FindMax(self):      # метод FindMax
        return max(self.inlst)

    def __add__(self, other):
        if len(self.inlst) == len(other.inlst):
            tmp = [(self.inlst[i]+other.inlst[i]) for i in range(len(self.inlst))]
            return tmp
        else:
            print("We CAN'T summ selected list becose they have different length")


print('Lets start with chose of length of list!')
n = int(input('Please, enter length of list: '))        #defining length of list

ls = IntList(n)         # creating object from class with length n

print("Now we must fill our list. Let's choose how we will do that: \n  1 - Manual input\n  2 - With RandomInt function")
choise = int(input('Enter number of you choose: '))
if choise == 1:
    ls.InputData()
elif choise == 2:
    ls.InputDataRandom()
else:
    print('Entered wrong number of choose! Please restart the program')

print('\n=> Call method prnt to see what we have in our list:')
ls.prnt()

print('\n=> Call method FindMax to see max value in list:')
print('Max value is:', ls.FindMax())

print('\n=> Call method FindValue to find indexes of value that we want to find:')
fv = int(input('Enter value that you want find in list: '))
ls.FindValue(fv)

print('\n=> Now we want call delete method. Lets choose with one we want to use:')
print('1 - Delete FIRST finded value\n2 - Delete ALL finded values')
choise = int(input('Enter number of you choose: '))
fv = int(input('Enter value that you want find and delete in list: '))
if choise == 1:
    ls.DelOneValue(fv)
    print('List after delete FIRST value', fv,'in list is:')
    ls.prnt()
elif choise == 2:
    ls.DelAllValues(fv)
    print('List after delete ALL values', fv, 'in list is:')
    ls.prnt()
else:
    print('Entered wrong number of choose! Please restart the program')

print('\n=> Now we want call __add__ method. To do it we create two randomly generated lists.')
i = int(input('Please, enter length of first  list: '))        #defining length of list
nl1 = IntList(i)
nl1.InputDataRandom()
nl1.prnt()
j = int(input('Please, enter length of second list: '))        #defining length of list
nl2 = IntList(j)
nl2.InputDataRandom()
nl2.prnt()
print('Lets try to summ them...')
print(nl1 + nl2)

print('\n=== Task #3 программа с классом Student ===')
def callName():     # func that promt to type name manualy
    name = input('Enter name of student: ')
    return name

def callAge():      # func that promt to type name manualy
    age = int(input("Enter student's age: "))
    return age

def callGroup():    # func that promt to type groupNumber manualy
    group = input("Enter group of student: ")
    return group

class Student:
    def __init__(self, name = 'Ivan', age = 18, groupNumber = '10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        print('Name: ', self.name)

    def getAge(self):
        print('Age:  ', self.age)

    def getGroupNumber(self):
        print('Group:', self.groupNumber)

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, group):
        self.groupNumber = group

    def prnt(self):         # def call of three methods in one
        self.getName()
        self.getAge()
        self.getGroupNumber()
        print("-----------------")


s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()
s5 = Student()

# Five times call setNameAge method with manual preset
s1.setNameAge('Alex', 17)
s2.setNameAge('Max', 18)
s3.setNameAge('Fill', 19)
s4.setNameAge('Bart', 20)
s5.setNameAge('Lisa', 21)

# Five times call setGroupNumber method with manual preset
s1.setGroupNumber('10A')
s2.setGroupNumber('11A')
s3.setGroupNumber('12A')
s4.setGroupNumber('13A')
s5.setGroupNumber('14A')

# # User typed change of params Name, Age, Group
# s1.setNameAge(callName(), callAge())
# s1.setGroupNumber(callGroup())
# s2.setNameAge(callName(), callAge())
# s2.setGroupNumber(callGroup())
# s3.setNameAge(callName(), callAge())
# s3.setGroupNumber(callGroup())
# s4.setNameAge(callName(), callAge())
# s4.setGroupNumber(callGroup())
# s5.setNameAge(callName(), callAge())
# s5.setGroupNumber(callGroup())

# print result prnt method uset three other get methods
s1.prnt()
s2.prnt()
s3.prnt()
s4.prnt()
s5.prnt()