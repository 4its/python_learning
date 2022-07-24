print('=== Task # 1 ===')
# Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом,
# то должна выполняться конкатенация, то есть соединение, строк. В остальных случаях введенные числа суммируются.
try:
    a = input('Enter first data:  ')
    b = input('Enter second data: ')
    a, b = float(a), float(b)
except ValueError:
    print("".join([a, b]))
else:
    print(a+b)
finally:
    print('Program is over. Thank you!')


print('\n=== Task # 2 ===')
# Нам нужно создать программу, которая позволяет создавать свои собственные PIN-коды для банковских карточек.
# Каждый PIN-код состоит из цифр. Дополните программу, чтобы в случае, когда пользователь вводит буквы,
# программа останавливалась и выводила "Please enter a number", а когда пользователь вводит только цифры,
# программа выводила PIN code is created".

try:
    a = input('Please enter a number: ')
    a = int(a)
except ValueError:
    print('Please enter a number.')
else:
    print('PIN code is created')