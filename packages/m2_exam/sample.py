from random import randint
from os import remove
import array as arr


class spisok:

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

    def set_atr(self, atr):
        self.atr = atr

    def fillrnd(self, strt=0, end=20):
        self.lst = (self.atr ,[randint(strt, end) for i in range(self.n)])

    def fillfromfile(self, file):
        try:
            nums_file = open(file, 'r')
            nums_file.close()
        except FileNotFoundError:
            print("Ups! You forget to create file! I'll generate it for you.")
            d = str()  # defining string
            for i in range(self.n):  # defining count of numers that we add in string with spaces between
                d = d + str(randint(a=0, b=20)) + ' '  # add randomly generated number in string
            print("Let's write this numbers to file:", d)
            file_nums = open(file, 'w')  # usr right 'w' to create file
            file_nums.write(d)  # write our string to file
            file_nums.close()  # close file
            print("File successfully generated. Lets read it!\n")
        nums_file = open(file, 'r')  # open file
        nums = list(nums_file.read().split())  # creating list of nubers from file
        nums_file.close()
        remove(file)
        self.lst = arr.array(self.atr,[int(nums[i]) for i in range(self.n)])


    def prnt(self):
        print(*self.lst)

    def findfirst(self, fv):
        # if fv not in self.lst:
        #     print('No value', fv, 'in list.')
        # else:
        #     for i,item in enumerate(self.lst):
        #         if item == fv:
        #             print('Found value',fv ,'at position', i)
        #             # return i          # as asked in task
        #             break
        return self.lst.index(fv)

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
        #print(*self.lst[1], sep=', ', end='.\n')

    def __add__(self, other):
        if len(self.lst) == len(other.lst):
            tmp = [(self.lst[i]+other.lst[i]) for i in range(len(self.lst))]
            print('Lists after summ:', tmp)
            # return tmp
        else:
            print("We CAN'T summ selected lst becose they have different length")

    # def __del__(self):              # destructor
    #     print('Object was deleted')


def numsgen(file):  # func to generate nums.txt if it doesn't exist with random numbers
    d = str()  # defining string
    for i in range(100):  # defining count of numers that we add in string with spaces between
        d = d + str(randint(a=0, b=20)) + ' '  # add randomly generated number in string
    print("Let's write this numbers to file:", d)
    file_nums = open(file, 'w')  # usr right 'w' to create file
    file_nums.write(d)  # write our string to file
    file_nums.close()  # close file
    print("File successfully generated. Lets read it!\n")


g = spisok(20)
g.set_atr('i')
g.fillrnd()
g.prnt()

j = spisok(20)
j.set_atr('i')
j.fillrnd()
j.prnt()

g + j
# print(g.findfirst(10))