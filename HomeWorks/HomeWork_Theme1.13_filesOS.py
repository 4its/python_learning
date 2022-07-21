from os import remove      # importing remove from OS for capability to delete files after close
from random import random  # importing random to use it in some functions


def numsgen(file):  # func to generate nums.txt if it doesn't exist with random numbers
    file_nums = open(file, 'w')  # usr right 'w' to create file
    d = str()  # defining string
    for i in range(int(random() * 100)):  # defining count of numers that we add in string with spaces between
        d = d + str((int(random() * 100))) + ' '  # add randomly generated number in string
    print("Let's write this numbers to file:", d)
    file_nums.write(d)  # write our string to file
    file_nums.close()  # close file
    print("File successfully generated. Lets read it!\n")

def sumnums(file):
    try:
        nums_file = open(file, 'r')
        nums_file.close()
    except FileNotFoundError:
        print("Ups! You forget to create file! I'll generate it for you.")
        numsgen(file)
    nums_file = open(file, 'r')             # open file
    nums = list(nums_file.read().split())   # creating list of nubers from file
    nums_file.close()                       # close file
    # remove(file)                            #delete file after close - thats will be more interest
    sum, i = 0, 0                           # simle counter and iterator
    while i < len(nums):
        sum += int(nums[1])                 # add number from list to summ
        i += 1
    print('Summ of numbers in file {0} is: '.format(file), sum)

def articlegen(file):  # func to generate article.txt if it doesn't exist with random numbers
    file_nums = open(file, 'w')  # usr right 'w' to create file
    d = str('Вечерело\nЖужжали мухи\nСветил фонарик\nКипела вода в чайнике\nВенера зажглась на небе\nДеревья шумели\nТучи разошлись\nЛиства зеленела')  # defining string
    print("Let's write this text to file:\n", d)
    file_nums.write(d)  # write our string to file
    file_nums.close()  # close file
    print("File successfully generated. Lets read it!\n")

def longest_words(file):
    try:
        art_file = open(file, 'r')
        art_file.close()
    except FileNotFoundError:
        print("Ups! You forget to create file! I'll generate it for you.")
        articlegen(file)
    art_file = open(file, 'r')
    article = list(art_file.read().split()) #creating list of words
    art_file.close()
    # remove(file)                            #delete file after close - thats will be more interest
    ml, i = 0, 0
    while i < len(article):                 #define maximum count of letter in word
        if len(article[i]) > ml:
            ml = len(article[i])
        i += 1
    i = 0
    print("Word(s) with maximum count of letters ({0}) in file {1} is:".format(ml, file), end=' ')
    while i < len(article):
        if len(article[i]) == ml:
            print(article[i], end=' ')  # printing word or words that have len == ml(Max count Letter)
        i += 1

def reverse(in_file, out_file):
    try:
        oif = open(in_file, 'r')
        oof = open(out_file, 'w')
        lines = oif.read().splitlines()
        i = len(lines)-1
        while i >= 0:
            oof.writelines(lines[i]+'\n')
            i-=1
        oof.close()
        print("File '{0}' successfuly reversed. You can see result in file '{1}'".format(in_file, out_file))
    except FileNotFoundError:
        print("File '{0}' not exist. Please, enter correct file name and restart program".format(in_file))

def pricegen(file):  # func to generate article.txt if it doesn't exist with random numbers
    file_nums = open(file, 'w')  # usr right 'w' to create file
    sample = ''
    for i in range(int(random()*100)):
        b = str(int(random()*10))
        print(type(b))
        c = str(float(random()*100))
        print(type(c))
        a = str("Custom Item {}\t{}\t{}\n".format(i,b,c))
        print(a)
        sample = sample + a
    print("Let's write this text to file:\n", sample)
    file_nums.write(sample)  # write our string to file
    file_nums.close()  # close file
    print("File '{0}' successfully generated. Lets read it!\n".format(file))

def total(in_file):
    try:
        oif = open(in_file, 'r')
        oif.close()
    except FileNotFoundError:
        print("Ups! You forget to create file! I'll generate it for you.")
        pricegen(in_file)
    oif = open(in_file, 'r')
    lines = list(oif.read().splitlines())
    oif.close()
    summ = 0.0  # def summ
    for line in lines:
        line = line.split('\t')
        summ += float(line[1]) * float(line[2])
    # print(lines)
    print("Total for order in '{}' is :{:.2f}".format(in_file, summ))


print('=== Task #1 файл nums.txt ===')
# Создайте файл nums.txt, содержащий несколько чисел, записанных через пробел.
# Напишите программу, которая подсчитывает и выводит на экран общую сумму чисел, хранящихся в этом файле
sumnums('nums.txt')             # if you select another file and it not exist - it will be created with random numbers

print('\n=== Task #2 файл article.txt===')
# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).
longest_words('article.txt')    # if you select another file and it not exist - it will be created from sample
print('')

print('\n=== Task #3 функция reverse ===')
# Напишите функцию reverse(in_file, out_file), которая читает строки из файла in_file и создает файл out_file,
# куда сохраняет прочитанные строки в обратном порядке.
reverse('article.txt', 'rev_article.txt')

print('\n=== Task #4 файле prices.txt ===')
# В многострочном текстовом файле prices.txt каждая строка с помощью символа табуляции разделена на три колонки:
# 1. название товара,
# 2. количество товара и
# 3. цена за 1 шт.
# Выведите общую стоимость заказа с точностью до копеек.
total('prices.txt')     # if you select another file and it not exist - it will be created
