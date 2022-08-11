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


