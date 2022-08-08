# Работа с файловой системой
f = open('../../files/example.txt', 'r')
f2 = open('../../files/example.txt', 'r+')
# print(*f)   # Выводит содержимое файла целиком
# print(f)    # выводим объект

# print(f.read(10))
# print('\n')
# print(f.read(200))

# print(f.readline())
# print('\n')
# print(f.readline())
# print('\n')
# print(f.readlines())
# f.seek(0)
# print(f.readline())

# f2.write('TEXT_ONE')
# f2.write('TEXT_TWO')
# print(f.readlines())
#
#
# f.close()   # закрывает файл
# f2.close()   # закрывает файл

import os
print("Текущая деректория:", os.getcwd())
os.chdir('/users/4its/')
print("Текущая деректория:", os.getcwd())
os.chdir('../../..')
print("Текущая деректория:", os.getcwd())

