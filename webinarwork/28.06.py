# # [] - list  - список   [4, 1, "Hello"]
# # () - tuple - кортеж   (4, 1, "Name")
# # {} - dict  - словарь  {"Name":"Alex", "age":19}
# # {} - множество {'a', 'r', 'b', 'w'}
#
# # left - >> rigth [0,1,2,3]
# # right - >> left [-4, -3, -2, -1]
#
#
# # list - список! в данном случае статический. Может хранить разные типы данных!
# #a = [12, 3.85, "black", 12, -4, "white", 12, 73, 101.2]
# #print("id ",id(a))
# #print(a[1:4])   # 1<=4
# #print(a[:4])   # 1<=4
# #print(a[1:])
# #print(a[:])
# #a.append(5)
# #a.insert(2, 'red')
# #print(a)
# #a.append(12)
# #print(a.index(12))
# #a.reverse()
# #print(a)
# #a.remove(12)
# #print(a)
# #b = a.count(12)
# #print(b)
#
# #b = a      #копирование - делается ссылка -    copy address
# #b = a[:]    #копирование срезом -               copy value
# #b[2]=28
#
# #print("id after change ",id(a))
# #print("id a ",id(a),"a ",a)
# #print("id b ",id(b),"b ",b)
#
# # () - tuple - кортеж
#
# #b = [(60, 90, 110),(23, 55, 86)]
# #a = (12, 3.85, "black", 12, -4, "white", 12, 73, 101.2)     #первый кортеж
# #b = a
# #print(type(b))
# #print(b)
# #c = (12, 3.85, ["black", 12, -4, "white", 12, 73], 101.2, b)
# #print(c)
# #c[2][4] = 'red'
# #print(c)
#
# # {} - dict  - словарь
# p_ages = {"Андрей": 32, "Виктор": 29, "Максим": 18}
# p_ages2 = {101: 32, 242: 29, "Максим": 18}
#
# print(p_ages)
# print(p_ages["Виктор"]) #29
# #print(p_ages[29]) #err
# print(p_ages2)
# print(p_ages2[242]) #29
# #print(p_ages2[29]) #err
#
# p_ages[55] = 17
# p_ages[36] = 17
# print(p_ages)
#
# p_ages["Анатолий"] = 17
# p_ages["Василий"] = 22
# print(p_ages)
# p_ages["Анатолий"] = 77
# print(p_ages)
# # print(p_ages + p_ages2)  #err!!!
# #p_ages = dict([(23,24),("Василий","Николай")])
# #print(p_ages)
# print(p_ages.get("Василий"))    #берем данные из словаря по ключу
# print(p_ages["Василий"])        #берем данные из словаря по ИНДЕКСУ
#
# #p_ages3 = p_ages
# p_ages3 = p_ages.copy()     #копирует значения и дальнейшие изменения не потянут изменение первоначального словаря
# p_ages3["Александр"] = 26   #в зависимости от способа копирования изменит/не_изменит и первоначальный!
# print(p_ages)
# print(p_ages3)
#
#
# # МНОЖЕСТВА
#
# one = { 32, 29, "Hello", "red", 55}
# print(one)

