print('=== Task #1 ===')

print('=== Task #2 ===')

class Home:
    def __init__(self, w, l, h):
        self.width = w
        self.length = l
        self.height = h

    def prnt(self):
        print('House params is:')
        print('wigth=', self.width)
        print('length=', self.length)
        print('height=', self.height)

    def setPeople(self):
        self.people = int(input('Enter number of people that live in this house: '))

    def setLanguage(self):
        self.language = (input('Enter language that people use in this house: '))

class City(Home):
    pass

h1 = City(3, 4, 5)
h1.prnt()