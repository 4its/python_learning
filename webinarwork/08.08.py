# class Car:
#
#     # create class attributes
#     name = "c200"
#     make = "mercedez"
#     model = 2008
#
#     # create class methods
#     # def set_name(self, a):
#     #     self.name = a
#
#     # def get_name()
#
#     def get_name(self):
#         print(self.name)
#
#     def get_horsepower(self):
#         self.hp = 210
#
#     def print_hp(self):
#         print(self.hp)
#
#     def start(self):
#         print ("Engine started")
#
#     def stop(self):
#         print ("Engine switched off")




#
# car_a = Car()
# car_b = Car()
#
# car_a.name = 's600'
#
# car_a.get_name()
# car_b.get_name()




# car_a.get_name()
# car_a.name = "s600"
# car_a.get_name()
# car_a.get_horsepower()
# print(car_a.hp)

# car_a.start()
# car_a.stop()


class Car:
    # create class attributes
    car_count = 0
    qqq = "Hello"
    # create class methods
    def __init__(self, name):
        self.name = name
        Car.car_count += 1
        print(Car.car_count)
        qqq = "Hello again"

    def start(self, make, model):
        print ("Engine started")
        self.make  = make
        self.model = model
        qqq = "Hello again again"
        # Car.car_count += 1

    def get_name(self):
        print(self.name)

    def stop(self):
        print("Engine switched off")


car_a = Car("Corrola")
car_a.start("Toyota", 2015)
print(car_a.name)
print(car_a.car_count)
print(car_a.qqq)

car_b = Car("City")
car_b.start("Honda", 2013)
print(car_b.name)
print(car_b.car_count)
print(car_b.qqq)






#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#
# a=Rectangle(10,20)
# print(a.area())
# #error#Rectangle.area()

