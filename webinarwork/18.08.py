# # class Table:
# #     def __init__(self, l=1, w=1, h=1):
# #         self.length = l
# #         self.width = w
# #         self.height = h
# #
# # class KitchenTable(Table):
# #     def __init__(self, p=2, l=0, w=0, h=0):
# #         Table.__init__(self, l, w, h)
# #         self.places = p
# #
# #     def prnt(self):
# #         print(self.places)
# #         print(self.length)
# #         print(self.width)
# #         print(self.height)
#
# class Table:
#     def __init__(self, l=1, w=1, h=1):
#         self.length = l
#         self.width = w
#         self.height = h
#         if isinstance(self, KitchenTable):
#             p = int(input("Сколькомест: "))
#             self.places = p
#
# class KitchenTable(Table):
#     def prnt(self):
#         print('places=', self.places)
#         print('length=', self.length)
#         print('width= ', self.width)
#         print('height=', self.height)
#
# t = Table()
# k = KitchenTable()
# k.prnt()

# # Create Class Vehicle
# class Vehicle:
#     def vehicle_method(self):
#         print("This is parent Vehicle class method")
# # Create Class Car that inherits Vehicle
# class Car(Vehicle):
#     def car_method(self):
#         print("This is child Car class method")
# # Create Class Cycle that inherits Vehicle
# class Cycle(Vehicle):
#     def cycleMethod(self):
#         print("This is child Cycle class method")
#
# car_a = Car()
# car_a.vehicle_method() # Calling parent class method
# car_b = Cycle()
# car_b.vehicle_method() # Calling parent class method

# class Camera:
#     def camera_method(self):
#         print("This is parent Camera class method")
#
#     def test(self):
#         print("This is PROBLEM!")
# class Radio:
#     def radio_method(self):
#         print("This is parent Radio class method")
#
#     def test(self):
#         print("This is NOT A PROBLEM!")
# class CellPhone(Camera, Radio):
#     def cell_phone_method(self):
#         print("This is child CellPhone class method")
#
# cell_phone_a = CellPhone()
# cell_phone_a.camera_method()
# cell_phone_a.radio_method()
# cell_phone_a.test()

from abc import ABC, abstractmethod


class Absclass(ABC):
    def print(self, x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

class test_class(Absclass):
    def task(self, value = 2):
        print("We are inside test_class task")
        print("Value =", value)

    @abstractmethod
    def my_method(self):
        pass

class example_class(test_class):
    def task(self):
        print("We are inside example_class task")
    def my_method(self):
        print('Print from example_clas - my_method')

example_obj = example_class()
example_obj.task()
example_obj.print(200)





#
# # t = Absclass()
# # t.print(18)
# #
# # t.task()
#
# #object of test_class created
# # test_obj = test_class()
# # test_obj.task()
# # test_obj.print(100)
#
# #object of example_class created
# example_obj = example_class()
# example_obj.task()
# example_obj.print(200)
# example_obj.my_method()

# class Robot:
#     def __init__(self, name):
#         self.name = name
#
# bb8 = Robot('BB-8')
# print(bb8.name)
# bb8.name = 'R2D2'
# print(bb8.name)

# class IPAddress:
#     def __init__(self, address, mask):
#         self._address = address
#         self._mask = int(mask)
#     def set_mask(self, mask):
#         if not isinstance(mask, int):
#             raise TypeError("Маска должна быть числом")
#         if not mask in range(8, 32):
#             raise ValueError("Маска должна быть в диапазоне от 8 до 32")
#         self._mask = mask
#     def get_mask(self):
#         return self._mask
#
# ip1 = IPAddress('10.1.1.1', 24)
# ip1.set_mask(23)
# print(ip1.get_mask())


# class IPAddress:
#     def __init__(self, address, mask):
#         self._address = address
#         self._mask = int(mask)
#     def set_mask(self, mask):
#         if not isinstance(mask, int):
#             raise TypeError("Маска должна быть числом")
#         if not mask in range(8, 32):
#             raise ValueError("Маска должна быть в диапазоне от 8 до 32")
#         self._mask = mask
#
#     @property
#     def get_mask(self):
#         return self._mask
#
#
# ip1 = IPAddress('10.1.1.1', 24)
# ip1.set_mask(23)
# print(ip1.get_mask)

# class IPAddress:
#     def __init__(self, address, mask):
#         self._address = address
#         self._mask = int(mask)
#
#     @property
#     def mask(self):
#         return self._mask
#
#     @mask.setter
#     def mask(self, mask):
#         if not isinstance(mask, int):
#             raise TypeError("Маска должна быть числом")
#         if not mask in range(8, 32):
#             raise ValueError("Маска должна быть в диапазоне от 8 до 32")
#         self._mask = mask
#
# ip1 = IPAddress('10.1.1.1', 24)
# print(ip1.mask)
# ip1.mask = 30
# print(ip1.mask)


# from datetime import date
# # random Person
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)
#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))
#
# person = Person('Adam', 19)
# person.display()
# person1 = Person.fromBirthYear('John', 1985)
# person1.display()

# class Mathematics:
#     def addNumbers(self, x, y):
#         return x + y
#
# # create add Numbers static method
# Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)
#
# print('The sum is:', Mathematics.addNumbers(5, 10))
