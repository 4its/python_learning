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
                n = int(input('Err: Value must be int and between 0 and 20: '))
                if 0 < n <= 20:
                    self.n = n
                else:
                    i = True

    def fillrnd(self, strt=0, end=20):
        self.lst = [randint(strt, end) for i in range(self.n)]

    def fillfromfile(self):
        pass


    def set_n1(self, n):
        n = int(input("Please, enter length of list:"))
        if 0 < n <= 20:
            self.n = n
        else:
            i = True
            while i == True:
                i = False
                n = int(input('Err: Value must be int and between 0 and 20: '))
                if 0 < n <= 20:
                    self.n = n
                else:
                    i = True

    def prnt(self):
        print(self.lst)

    def findfirst(self, fv):
        if fv not in self.lst:
            print('No value', fv, 'in list.')
        else:
            for i,item in enumerate(self.lst):
                if item == fv:
                    print('Found value',fv ,'at position', i)
                    # return i          # as asked in task
                    break

    def findall(self, fv):
        if fv not in self.lst:
            print('No value', fv, 'in list.')
        else:
            tmp = [i for i, item in enumerate(self.lst) if item == fv]
            print("Value", fv, "founded in next place(s):", *tmp)
            # return tmp            # as asked in task

    def delfv(self, fv):            # Delete FIRST finded value in list
        if fv not in self.lst:
            print('Value', fv, 'not in list.')
        else:
            self.lst.remove(fv)
            self.prnt()             #output after delete

    def delallv(self, fv):          # Delete ALL finded values in list
        if fv in self.lst:
            tmp = [i for i, item in enumerate(self.lst) if item == fv]
            for item in reversed(tmp):
                self.lst.pop(item)
            self.prnt()             #output after delete
        else:
            print('Value', fv, 'not in list.')

    def prnt(self):
        print(self.lst)

    def __add__(self, other):
        if len(self.lst) == len(other.lst):
            tmp = [(self.lst[i]+other.lst[i]) for i in range(len(self.lst))]
            print('Lists after summ:', tmp)
            # return tmp
        else:
            print("We CAN'T summ selected lst becose they have different length")

    # def __del__(self):              # destructor
    #     print('Object was deleted')