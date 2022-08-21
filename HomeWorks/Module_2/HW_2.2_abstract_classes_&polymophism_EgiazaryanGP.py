from abc import ABC, abstractmethod
print('=== Task #1 ===')

print('=== Task #2 написать абстрактный класс Home===')

class Home(ABC):
    def __init__(self, w, l, h):
        self.width = w
        self.length = l
        self.height = h

    @abstractmethod
    def prnt(self):
        print('House params is:')
        print('wigth=', self.width)
        print('length=', self.length)
        print('height=', self.height)

    @abstractmethod
    def setPeople(self):
        self.people = int(input('Enter number of people that live in this house: '))

    @abstractmethod
    def setLanguage(self):
        i = True
        while i == True:
            i = False
            lng = int(input('Please, choose language:\n1 - Russian\n2 - English\nWhat do you choose: '))
            if lng == 1:
                self.language = 'Russian'
            elif lng == 2:
                self.language = 'English'
            else:
                i = True
                print('Wrong choose!')

class City(Home):
    pass


h1 = City(3, 4, 5)
h1.setLanguage()