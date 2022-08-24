from random import randint
from os import remove
import array as arr
import json


class Spisok:

    def __init__(self, n, atr='i'):          # constructor
        self.atr = atr
        if 0 < n <= 50:
            self.n = n
        else:
            i = True
            while i:
                i = False
                n = int(input('Err: Value must be int and between 0 and 50: '))
                # self.n = n if 0 < n <= 50 else i = True        # Didn't work =(
                if 0 < n <= 50:
                    self.n = n
                else:
                    i = True

    def set_atr(self, atr):  # method to change atr of array (fillers will not work with others types of arrays)
        self.atr = atr       # if we want to use others types of arrays - we neet to add some way thought IF operator

    def fillrnd(self, strt=0, end=20):          # use randint func to fill array. Default range is 0,20
        self.lst = arr.array(self.atr, [randint(strt, end) for i in range(self.n)])

    def fillfromfile(self, file, strt=0, end=20):
        try:
            nums_file = open(file, 'r')
            nums_file.close()
        except FileNotFoundError:
            print("Ups! You forget to create file! I'll generate it for you.")
            d = str()  # defining string
            for i in range(self.n * 2):  # defining count of numers that we add in string with spaces between
                d = d + str(randint(strt, end)) + ' '  # add randomly generated number in string
            print("Let's write this numbers to file:", d)
            file_nums = open(file, 'w')  # usr right 'w' to create file
            file_nums.write(d)  # write our string to file
            file_nums.close()  # close file
            print("File successfully generated. Lets read it and took", self.n, "from it!")
        nums_file = open(file, 'r')  # open file
        nums = list(nums_file.read().split())  # creating list of nubers from file
        nums_file.close()
        remove(file)      # Will remove file after close
        self.lst = arr.array(self.atr, [int(nums[i]) for i in range(self.n)])

    def wr2file(self, file):        # Use json library to write array into file
        with open(file, 'w') as file:
            json.dump(self.lst.tolist(), file)

    def wrFromFile(self, file):     # Use json to read file that was written by wr2file method
        with open(file, 'r') as file:
            self.lst = arr.array(self.atr, json.load(file))

    def prnt(self):
        print(self.lst)

    def findfirst(self, fv):
        # if fv not in self.lst:
        #     print('No value', fv, 'in array.')
        # else:
        #     print('Found value',fv ,'at position', self.lst.index(fv))
        print('No value', fv, 'in array.') if fv not in self.lst else print('Found value', fv, 'at position',
                                                                            self.lst.index(fv))

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
            print('deleted value', fv, 'in array! Array after delete below')
            self.prnt()             # output after delete

    def delallv(self, fv):          # Delete ALL finded values in list
        if fv in self.lst:
            tmp = [i for i, item in enumerate(self.lst) if item == fv]
            for item in reversed(tmp):
                self.lst.pop(item)
            self.prnt()             # output after delete
        else:
            print('Value', fv, 'not in list.')

    def prnt(self):
        print(self.lst)
        # print(*self.lst[1], sep=', ', end='.\n')

    def intersection(self, other):
        tmp = []
        for item in self.lst:
            if item in other.lst and item not in tmp:
                tmp.append(item)
        print(tmp)
        tmp = arr.array(self.atr, tmp)
        return tmp

    def __add__(self, other):
        # if self.lst[0] == other.lst[0] and len(self.lst[1]) == len(other.lst[1]):
        #     self.tmp1, other.tmp1 = self.lst[1], self.lst[1]
        #     tmp = arr.array(self.atr, [(self.tmp1[i]+other.tmp1[i]) for i in range(len(self.tmp1))])
        if len(self.lst) == len(other.lst):
            tmp = arr.array(self.atr, [self.lst[i] + other.lst[i] for i in range(len(self.lst))])
            print('Lists after summ:        ', tmp)
            # return tmp
        else:
            print("We CAN'T summ selected lists becose they have different length")
            # return "We CAN'T summ selected lists becose they have different length"

    def __del__(self):              # destructor
        print('Object was deleted')


print('==arr1==')
g = Spisok(25)
# g.set_atr('i')      # Not defined fillers to others types of arrays, but all other methos will work with them
g.fillrnd()         # filling by randint function. You may add some attribute like g.fillrnd(1,100) to it.
g.findfirst(10)     # try to find first value 10 in first array
g.prnt()            # print our array
g.delfv(5)          # try to delete firs found value 5 in array. If we haven't them we will see message about it

print('\n==arr2==')

j = Spisok(25)
j.fillfromfile('list2.txt')   # filling by randint function. You may add some attribute like j.fillfromfile('list2.txt', 1, 100)  to it
j.prnt()            # print our array
j.findall(10)       # try to find ALL values 10 in second array
j.delallv(7)        # try to delete ALL founded value 7 in array. If we haven't them we will see message about it


g.wr2file('arr1.txt')
j.wr2file('arr2.txt')

print('\nArray of intersection values for both arrays is: ', g.intersection(j))

print('\n==Trying to summ our arrays==')
print('Finnaly we have array1:   ', end='')
g.prnt()
print('Finnaly we have array2:   ', end='')
j.prnt()

g + j

print('\n== Destructor time ===')
