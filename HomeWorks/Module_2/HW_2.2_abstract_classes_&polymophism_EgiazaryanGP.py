from abc import ABC, abstractmethod
from math import pi

print('=== Task #1 Написать абстрактный класс – фигура ===')
# class figure(ABC):
#     @abstractmethod
#     def prnt(self):
#         pass
#
#     @abstractmethod
#     def setColor(self):
#         pass
#
# class dot(figure):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def prnt(self):
#         print('x =', self.x)
#         print('y =', self.y)
#
#     def setColor(self):
#         self.color = input('Enter name of color for this object:')
#
# class circle(dot):
#     def __init__(self, x, y, r, c = 'white (default)'):
#         self.x = x
#         self.y = y
#         self.r = r
#         self.color = c
#
#     def prnt(self):
#         print('\nCircle param is:')
#         dot.prnt(self)
#         print('radius is: ',self.r)
#         print('color is:  ', self.color)
#
#     # setColor method will be inherited from dot class
#     def circleS(self):
#         print('Area of circle is: ', pow(pi * self.r, 2))
#
#     def setRadius(self, r):
#         self.r = r
#
# class sphere(circle):
#     def __init__(self, x, y, rs, rb, c = 'white (default)'):
#         self.x = x
#         self.y = y
#         self.rs = rs
#         self.rb = rb
#         self.color = c
#
#     def prnt(self):
#         print('\nSphere param is:')
#         dot.prnt(self)
#         print('s_radius is: ',self.rs)
#         print('b_radius is: ', self.rb)
#         print('color is:  ', self.color)
#
#     # setColor method will be inherited from dot Circle => Dot classes
#
#     def circleS(self):
#         print('Area of sphere is: ', 4 * pi * pow(self.rb, 2))
#
#     def setRadius(self, rs, rb):
#         self.rs = rs
#         self.rb = rb
#
#
# cir = circle(1, 1, 5)       # creating object from circle class
# # cir.setColor()              # changing color(default is white
# cir.prnt()                  # printing his params
# cir.circleS()               # printing area of circle
#
# sp = sphere(1,1, 5, 10)     # creating object from sphere class
# # sp.setColor()               # changing color(default is white
# sp.prnt()                   # printing his params
# sp.circleS()                # printing area of sphere


print('\n=== Task #2 написать абстрактный класс Home===')

# class Home(ABC):
#     def __init__(self, w, l, h):
#         self.width = w
#         self.length = l
#         self.height = h
#
#     @abstractmethod
#     def prnt(self):
#         print('House params is:')
#         print('wigth=', self.width)
#         print('length=', self.length)
#         print('height=', self.height)
#
#     @abstractmethod
#     def setPeople(self):
#         self.people = int(input('Enter number of people that live in this house: '))
#
#     @abstractmethod
#     def setLanguage(self):
#         i = True
#         while i == True:
#             i = False
#             lng = int(input('Please, choose language:\n1 - Russian\n2 - English\nWhat do you choose: '))
#             if lng == 1:
#                 self.language = 'Russian'
#             elif lng == 2:
#                 self.language = 'English'
#             else:
#                 i = True
#                 print('Wrong choose!')
#
#
# class City(Home, ABC):
#     def __init__(self, w, l, h, p, lng, cnt_houses):
#         self.width = w
#         self.length = l
#         self.height = h
#         self.people = p
#         self.language = lng
#         self.houses_in_city = cnt_houses
#
#     @abstractmethod
#     def prnt(self):
#         print('Houses params is:')
#         print('wigth=', self.width)
#         print('length=', self.length)
#         print('height=', self.height)
#         print('People in one house is: ', self.people)
#         print('Language in houses is: ', self.language)
#         print('Number of houses in city is:', self.houses_in_city)
#
#     def setCount(self):
#         self.houses_in_city = int(input('   Enter number of houses in city: '))
#
#     def setPeople(self):
#         self.people = int(input('   Enter number of people that live in this house: '))
#
#     def setLanguage(self):
#         i = True
#         while i == True:
#             i = False
#             lng = int(input('Please, choose language:\n1 - Russian\n2 - English\nWhat do you choose: '))
#             if lng == 1:
#                 self.language = 'Russian'
#             elif lng == 2:
#                 self.language = 'English'
#             else:
#                 i = True
#                 print('Wrong choose!')
#
# class Country(City):
#     def __init__(self, w, l, h, p, lng, cnt_houses, cnt_city):
#         self.width = w
#         self.length = l
#         self.height = h
#         self.people = p
#         self.language = lng
#         self.houses_in_city = cnt_houses
#         self.city_in_country = cnt_city
#
#     def prnt(self):
#         print('Houses params is:')
#         print(' wigth is:', self.width)
#         print('length is:', self.length)
#         print('height is:', self.height)
#         print('Language in houses is: ', self.language)
#         print('People in one house is:        ', self.people)
#         print('Number of houses in city is:   ', self.houses_in_city)
#         print('Number of cities in Country is:', self.city_in_country)
#
#     def CountPeople(self):
#         print('    Number of people that live in country is:', self.city_in_country * self.houses_in_city * self.people)
#
#     # Next methods will be inherited from the сity class !!!
#     # def setCount(self):
#     #     self.houses_in_city = int(input('Enter number of houses in city: '))
#     #
#     # def setPeople(self):
#     #     self.people = int(input('Enter number of people that live in one house: '))
#     #
#     # def setLanguage(self):
#     #     i = True
#     #     while i == True:
#     #         i = False
#     #         lng = int(input('Please, choose language:\n1 - Russian\n2 - English\nWhat do you choose: '))
#     #         if lng == 1:
#     #             self.language = 'Russian'
#     #         elif lng == 2:
#     #             self.language = 'English'
#     #         else:
#     #             i = True
#     #             print('Wrong choose!')
#
#
# task2_obj = Country(3, 4, 5, 3, 'Russian', 10, 5)      # creating object from Country class
# task2_obj.prnt()                                       # printing params of object
# task2_obj.setCount()                                   # changing nuber of houses in city
# task2_obj.prnt()                                       # printing params of object again (to see what we change(or not))
# task2_obj.setPeople()                                  #changinf number of people in one house
# task2_obj.prnt()                                       # printing params of object
# task2_obj.CountPeople()                                # count people in country

print('\n=== Task #3 ===')

class Game:
    pass


