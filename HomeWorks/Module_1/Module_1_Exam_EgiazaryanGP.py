from random import randrange    # importing generator of random numbers IN RANGE!


def lengthoflist():
    # размер списка числе определяется пользователем программы.
    # Выполнить контроль ввода информации – число должно быть положительное и не более 20
    while True:
         try:
             n = int(input('Enter length of list:'))
             if n > 0 and n <= 20:
                 return n
                 False
             else:
                 print('Entered lenght must be greater than 0 and less or equal 20.')
         except ValueError:
             print('Numbers only allowed. Please, retype!')

def filllist(n):
    # заполнение списка осуществляется на основе датчика случайных чисел и реализация осуществляется в виде функции,
    # которой в качестве аргумента указывается размер списка
    return [int(randrange(100)) for i in range(n)]

def printlist(list):        # printig list as list
    # реализация печати элементов списка осуществляется в виде функции,
    # которой в качестве аргумента указывается список чисел
    print('Generated list is:', list)

def printlistv(list):       # printing values from list in row, separated by spaces
    # реализация печати элементов списка осуществляется в виде функции,
    # которой в качестве аргумента указывается список чисел
    print('Values in generated list is:', *list)

def printlistv2(list):      # printing values from list by clasic print+cycle FOR funnctiot
    # реализация печати элементов списка осуществляется в виде функции,
    # которой в качестве аргумента указывается список чисел
    print('Values in generated list is:')
    for element in list:
        print(element)

def findvalue(list, value):
    # реализация поиска заданного элемента списка осуществляется в виде функции,
    # которой в качестве аргумента указывается список чисел, и искомое число.
    # Функция возвращает результат – номер позиции где впервые найден данный элемент
    if value in list:
        print('Index of value', value, 'in list is:', list.index(value))      # more beautiful output
        # return list.index(value)                                          # output like asked in task
    else:
        print('Value', value, 'not in list.')

def deffindvalue():
    while True:
         try:
             n = int(input('Enter value that you want find in list(Only numbers allowed): '))
             if n > 0:
                 return n
                 False
             else:
                 print('Entered value must be greater than 0.')
         except ValueError:
             print('Numbers only allowed. Please, retype!')

def defdelvalue():
    while True:
         try:
             n = int(input('Enter value that you want delete from list(Only numbers allowed): '))
             if n > 0:
                 return n
                 False
             else:
                 print('Entered value must be greater than 0.')
         except ValueError:
             print('Numbers only allowed. Please, retype!')

def findvalueindexes(list, value):
    # реализация поиска заданного элемента с указанием всех позиций нахождения в списке осуществляется в виде функции,
    # которой в качестве аргумента указывается список чисел, и искомое число.
    # Функция возвращает результат – список номеров позиций где найден данный элемент
    if value in list:
        tmp = []
        for i, item in enumerate(list):
            if item == value:
                tmp.append(i)
        print('Indexes of',value, 'in list is:', *tmp)          # more beautiful output
        # return tmp                                            # output like asked in task
    else:
        print('Value', value, 'not in list.')

def deletevalue(list, value):       # func that delete FIRST values in list
    # реализация удаление заданного элемента в списке осуществляется в виде функции,
    # которой в качестве аргумента указывается список чисел, и искомое число.
    # Функция возвращает результат – список без указанного элемента
    print('List before delete:', list)
    if value in list:
        list.remove(value)
        print('List after delete: ', list)              # more beautiful output
        # print(list)                                   # output like asked in task
    else:
        print('Value', value, 'not in list.')

def deletevalueall(list, value):    # func that delete ALL values in list       (Additional func)
    # реализация удаление заданного элемента в списке осуществляется в виде функции,
    # которой в качестве аргумента указывается список чисел, и искомое число.
    # Функция возвращает результат – список без указанного элемента
    list_ = list[::]
    print('List before delete:', list_)
    if value in list_:
        for item in list_:
            if item == value:
                list_.remove(item)
        print('List after delete: ', list_)              # more beautiful output
        # return list                                   # output like asked in task
    else:
        print('Value', value, 'not in list.')

def summlists(list1, list2):
    # реализация сложения списков чисел осуществляется в виде функции,
    # которой в качестве аргумента указывается списки чисел.
    # Функция возвращает результат – печать на экране сообщения «сложение невозможно,
    # из-за несовпадения длин списков», или список, в котором выполнено сложение поэлементно двух заданных списков чисел
    tmp = []
    if len(list1) == len(list2):
        i, n = 0, len(list1)
        while i < len(list1):
            tmp.append(list1[i]+list2[i])
            i+=1
        print('List of summs is:', tmp)             # more beautiful output
        # return tmp                                # output like asked in task
    else:
        print('сложение невозможно, из-за несовпадения длин списков')


print('Filling list #1 by random values between 0 and 100.')
list1 = filllist(lengthoflist())    # creating list #1 and filling them
printlist(list1)                    # printing list with a function
printlistv(list1)                   # printing VALUES from list with a function(in row, separated by spaces)
# printlistv2(list1)                  # printing values from list by classic print+cycle FOR function
print('\n')

print('Filling list #2 by random values between 0 and 100.')
list2 = filllist(lengthoflist())    # creating list #2 and filling them
printlist(list2)                    # printing list with a function
printlistv(list2)                   # printing VALUES from list with a function(in row, separated by spaces)
# printlistv2(list2)                  # printing values from list by classic print+cycle FOR function
print('\n')

#Finding value in list1 and list2
# print('Finding value in list1 and list2')
findvalue(list1, deffindvalue())
findvalue(list2, deffindvalue())
print('\n')

#Finding indexes of value in list1 and list2
# print('Finding indexes of value in list1 and list2')
findvalueindexes(list1, deffindvalue())
findvalueindexes(list2, deffindvalue())
print('\n')

# Delete FIRST value in list1 and list2
# print('Delete FIRST value in list1 and list2')
deletevalue(list1,defdelvalue())
deletevalue(list2,defdelvalue())
print('\n')

# Delete ALL values in list1 and list2     ( Additional )
# print('Delete ALL values in list1 and list2     ( Additional )')
deletevalueall(list1,defdelvalue())
deletevalueall(list2, defdelvalue())
print('\n')

# summ of lists
# print('Summ of lists')
summlists(list1, list2)     #summ of existed lists
print('\n')
summlists(filllist(lengthoflist()),filllist(lengthoflist()))        #summ of new list
