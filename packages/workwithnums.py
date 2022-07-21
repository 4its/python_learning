def max_min(a=1, b=2):
    if a > b:
        print('\nMaximum for numbers', a, 'and', b, 'is:', a)
    else:
        print('\nMaximum for numbers', a, 'and', b, 'is:', b)

def even_odd(a, b):
    if (a % 2) == 0:
        print('\nNumber', a, 'is EVEN')
    else:
        print('\nNumber', a, 'is ODD')
    if (b % 2) == 0:
        print('Number', b, 'is EVEN')
    else:
        print('Number', b, 'is ODD')

def summ(a, b):
    print('\nSumm of numbers', a, 'and', b, 'is:', a+b)

def division5(a, b, c=5):
    if ((a % c) == 0) & ((b % c) == 0):
        print('\nNumbers', a, 'and', b, 'can be divisioned by', c)
    elif ((a % c) == 0) & ((b % c) != 0):
        print('\nOnly number', a, 'can be divisioned by', c)
    elif ((a % c) != 0) & ((b % c) == 0):
        print('\nOnly number', b, 'can be divisioned by', c)
    else:
        print('\nNumbers', a, 'and', b, "can't be divisioned by", c)

def sqr(a, b):
    print('\nSquared number', a, 'is', a * a)
    print(  'Squared number', b, 'is', b * b)
