from m2_exam import *       # import package


a = spisok(20)      # using class to create obj
b = spisok(20)      # using class to create obj
a.fillrnd()         # fill obj a by rnd func
b.fillrnd()         # fill obj b by file
a.prnt()            # print list a
b.prnt()            # print list b
a.findfirst(5)      # find first value 5 in list
b.findall(11)       # find all values 11 in list

a.delfv(5)          # del first value 5 in list
a.delallv(7)        # del ALL values 7 in list


a + b               # try to summ list a and b