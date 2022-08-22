# class Car:
#     # create class attributes
#     car_count = 0
#     test1 = 'Hello'
#     # create class methods
#     def __init__(self, name, make):
#         self.name = name
#         self.make = make
#         Car.car_count += 1
#         print('Car_count is:',Car.car_count)
#
#
#     def start(self, model):
#         print ("Engine started")
#         self.model = model
#
#     def get_name(self):
#         name = self.name
#         return name
#
#     def get_make(self):
#         make = self.make
#         return make
#
#     # def get_model(self):
#     #     model = self.model
#     #     return model
#
#     def my_method(self):
#         pass
#
#     def __add__(self, other):
#         return Car(self.name + other.name, self.make + other.make)
#
#
# car_a = Car("Corrola", "Toyota")
# # car_a.start(2015)
#
# car_b = Car("Civic", "Honda")
# # car_b.start(2013)
#
# car_c = car_a + car_b
#
# print(car_c.get_name())
# print(car_c.get_make())
# # print(car_c.get_model())
#


# class B:
#     __count = 0
#     def __init__(self):
#         B.__count += 1
#     def __del__(self):
#         B.__count -= 1
#     def __test(self):
#         print('method test work')
#
#
# a = B()
# b = B()
# print(B._B__count)
# # del a
# print(B._B__count)
# B._B__test(B)


#
# class Car:
#     # publ = 'public'
#     # _prot = 'protected'
#     # __priv = 'private'
#
#     message1 = "Engine started"
#     def _test(self):
#         print('проверка работы систем')
#     def start(self):
#         message2 = "Car started"
#         self._test()
#         return message2
#
# car_a = Car()
# print(car_a.start())
# car_a._test()

# class Person:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.__age = age
#     def display(self):
#         print(self.name)
#         print(self.__age)
#
#     def getAge(self):
#         print(self.__age)
#     def setAge(self, age):
#         # missed checkin of entered params
#         self.__age = age
#
#
# person = Person('Dev', 30)
# person2 = Person('Alex', 30)
#
# person.display()
# person.setAge(35)
# person.getAge()


# PART 2

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
#     def make_sound(self):
#         print("Meow")
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
#     def make_sound(self):
#         print("Bark")
#
# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)
#
# animal_list = [cat1, dog1]
#
# for animal in (cat1, dog1): # can write for animal in (animal_list):...
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()


# from math import pi
#
# class Shape:
#     def __init__(self, name):
#         self.name = name
#     def area(self):
#         pass
#     def fact(self):
#         return "I am a two-dimensional shape."
#     def __str__(self):
#         return self.name
#
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length
#     def area(self):
#         return self.length**2
#     def fact(self):
#         return "Squares have each angle equal to 90 degrees."
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius
#     def area(self):
#         return pi*self.radius**2
#
# a = Square(4)
# b = Circle(7)
# print(b)
# print(b.fact())
# print(a.fact())
# print(b.area())


# class Table:
#     def __init__(self, l, w, h):
#         self.length = l
#         self.width = w
#         self.height = h
#
# class DeskTable(Table):
#     def square(self):
#         return self.width * self.length
#
#
# t1 = Table(1.5, 1.8, 0.75)
# t2 = DeskTable(0.8, 0.6, 0.7)
# print(t2.square())
# t2.length = 2
# print(t2.square())

# class Table:
#     def __init__(self, l, w, h):
#         self.length = l
#         self.width = w
#         self.height = h
# class DeskTable(Table):
#     def square(self):
#         return self.width * self.length
#     def __init__(self, l, w, h, c):
#         self.length = l
#         self.width = w
#         self.height = h
#         self.color=c
# t1 = Table(1.5, 1.8, 0.75)
# t2 = DeskTable(0.8, 0.6, 0.7, "Blue")
# print(t2.color) # color print(t2.square())

# class Table:
#     def __init__(self, l, w, h):
#         self.length = l
#         self.width = w
#         self.height = h
#
# class DeskTable(Table):
#     def square(self, monitor):
#         print('calculate DeskTable')
#         # return self.width * self.length
#         return self.width * self.length #- monitor
#
#
# class ComputerTable(DeskTable):
#     def square(self, monitor=0.0):
#         print('calculate ComputerTable')
#         return self.width * self.length #- monitor
#
# t3 = ComputerTable(0.8, 0.6, 0.7)
# print(t3.square(0.3)) # вывод: 0.18

class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        #Table.__init__(self, l, w, h)   # not preffered
        super().__init__(l, w, h)       # preffered choise in THAT case
        self.places = p


t4 = KitchenTable(1.5, 2, 0.75, 6)