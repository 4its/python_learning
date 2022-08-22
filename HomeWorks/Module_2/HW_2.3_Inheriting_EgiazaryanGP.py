from math import pi

print('=== Task #1  ===')


# class dot:
#     def __init__(self, x, y, c='white (by Default)'):
#         self.x = x
#         self.y = y
#         self.color = c      # setting default color
#
#     def prnt(self):
#         print('x =', self.x)
#         print('y =', self.y)
#
#     def setColor(self):
#         self.color = input('Enter name of color for this object:')
#
#
# class circle(dot):
#     def __init__(self, x, y, r, c='white (default)'):
#         super(circle, self).__init__(x, y, c)
#         self.r = r
#
#     def prnt(self):
#         print('\nCircle param is:')
#         dot.prnt(self)
#         print('radius is: ', self.r)
#         print('color is:  ', self.color)
#
#     def setColorС(self):
#         super(circle, self).setColor()      #this methoc calls to DOT class. Also we can call "setColor" method from DOT class with same result
#
#     def circleS(self):
#         print('Area of circle is: ', pow(pi * self.r, 2))
#
#     def setRadius(self, r):
#         self.r = r
#
#
# class sphere(circle):
#     def __init__(self, x, y, rs, rb, c='white (default)'):
#         super(circle, self).__init__(x, y, c)
#         self.rs = rs
#         self.rb = rb
#
#     def prnt(self):
#         print('\nSphere param is:')
#         dot.prnt(self)
#         print('s_radius is: ', self.rs)
#         print('b_radius is: ', self.rb)
#         print('color is:  ', self.color)
#
#     # setColor method will be inherited from dot Circle => Dot classes
#     # setColorC method will be also inherited from dot Circle => Dot classes
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
# cir.prnt()                  # printing his params
# cir.setColorС()             # Try to change color of circle
# cir.prnt()                  # printing his params again
# cir.circleS()               # printing area of circle
#
# sp = sphere(2, 2, 7, 10)     # creating object from sphere class
# sp.prnt()                   # printing his params
# sp.setColorС()              # Try to change color of sphere
# sp.prnt()                   # printing his params again
# sp.circleS()                # printing area of sphere

print('\n=== Task #2  ===')

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def prnt(self):
        print('Book title:    ', self.title)
        print('Book author:   ', self.author)
        print('Pages in book: ', self.pages)

    def setName(self):
        self.title = input('Enter new title of book: ')     # simple set name =)

    def price(self, prc = 2.5):
        #print("Price for book -",self.title, "(",self.pages ,"pages ) is -", self.pages * prc, "rub.")
        return self.pages * prc


class publishing_house(Book):
    def __init__(self, title, author, pages, c, lng = 'Russian (by Default)'):
        super(publishing_house, self).__init__(title, author, pages)
        self.circulation = c
        self.language = lng

    def prnt(self):
        super(publishing_house, self).prnt()
        print('Book circulation:', self.circulation, 'copies')
        print('Book language:   ', self.language)

    def setPr(self):
        self.circulation = int(input("Enter nuber of copies of book that you want to print(must be int): "))

    def setLanguage(self):
        i = True
        while i == True:
            i = False
            lng = int(input('Please, choose language:\n1 - Russian\n2 - English\n3 - German\nWhat do you choose: '))
            if lng == 1:
                self.language = 'Russian'
            elif lng == 2:
                self.language = 'English'
            elif lng == 3:
                self.language = 'German'
            else:
                i = True
                print('Wrong choose!')

    def priceAll(self):
        return self.price() * self.circulation      #used default price from book class(is 2.5)

##Checking Book class
book1 = Book('The Mysterious Island', 'Jules Verne', 952)
book1.prnt()
print("Price for book -",book1.title, "(",book1.pages ,"pages ) is -", book1.price(), "rub.")

print('\n')         #spacer

##Checking Publishing_house class
book2 = publishing_house('20000 Leagues Under the Sea', 'Jules Verne', 514, 20000)
book2.prnt()
book2.setPr()           # not added checking of entered value... If it needed I'll do it
book2.prnt()
print("Price for book -",book2.title, "(",book2.pages ,"pages ) is -",
      book2.price(), "rub.")   # Inherited method from book class
print("Price for calculation of book",book2.title, "(",book2.pages ,"pages,",
      book2.circulation,"copies ) is -", book2.priceAll(), "rub.") # Use method priceAll in publishing_house class
