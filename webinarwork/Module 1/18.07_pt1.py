import os
# вывести текущую директорию
# print("Текущая деректория:", os.getcwd())
# # повторный запуск mkdir с тем же именем вызывает FileExistsError, # вместо этого запустите:
# if not os.path.isdir("folder"):
#     os.mkdir("folder")
# print(os.listdir())

# print("Текущая деректория:", os.getcwd())
# # распечатать все файлы и папки рекурсивно
# for dirpath, dirnames, filenames in os.walk("."):
#     # перебрать каталоги
#     for dirname in dirnames:
#         print("Каталог:", os.path.join(dirpath, dirname))
#     # перебрать файлы
#     for filename in filenames:
#         print("Файл:", os.path.join(dirpath, filename))

import sys
# print(f'Hello {sys.argv[1]}')
# print('\n')
# print(f'Hello {sys.argv[2]}')

# if len(sys.argv) == 1:
#     print('Привет мир!')
# else:
#     print(f'Привет {sys.argv[1]}')

# if len(sys.argv) == 1:
#     print('Привет мир!')
# else:
#     p_name = sys.argv[1]
#     p_value = sys.argv[2]
#     if p_name == '--name':
#         print(f'Привет {p_value}')
#     else:
#         print(f'Неизвесный параметр {p_name}')

import argparse
# parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(
prog='Greeting Script',
description='Программа, которая говорит "Привет"', epilog='(c) Информация об авторе программы')

# parser.add_argument('name', nargs='?', default='мир!')
parser.add_argument('-name', '-n', nargs='?', default='мир!', help='Позволяет добавить имя в качетстве аргумента')
parser.add_argument('-surname', '-surn', nargs='?', default='мир!', help='Позволяет добавить фамилию в качетстве аргумента')
args = parser.parse_args()
print(f'Привет {args.name} {args.surname}')
