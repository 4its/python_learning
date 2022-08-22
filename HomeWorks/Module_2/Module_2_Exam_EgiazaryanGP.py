from random import randint


class spisok:

    lst = []

    def __init__(self, n):          # constructor
        if 0 < n <= 20:
            self.n = n
        else:
            i = True
            while i == True:
                i = False
                n = int(input("Please, enter length of list:"))



    # def __del__(self):              # destructor
    #     print('Object was deleted')

    def fillrnd(self, strt=0, end=10):
        self.lst = [randint(strt, end) for i in range(self.n)]

    def prnt(self):
        print(self.lst)

    def __add__(self, other):
        if len(self.lst) == len(other.lst):
            tmp = [(self.lst[i]+other.lst[i]) for i in range(len(self.lst))]
            return tmp
        else:
            print("We CAN'T summ selected lst becose they have different length")


a = spisok(110)
a.prnt()
a.fillrnd()
a.prnt()
