def triangle_perimeter(a=7, b=2, c=8):
    return a + b + c


def triangle_area(a=7, b=2, c=8):
    p = (triangle_perimeter(a=a, b=b, c=c)) / 2
    s = pow((p * (p - a) * (p - b) * (p - c)), 0.5)
    return s


def triangle_define(a=7, b=2, c=8):
    if (a == b) & (b == c) & (c == a):
        print('Triangle with sides: a',a,b,c,'is equilateral triangle (равносторонний)')
    elif (a == b) | (b == c) | (c == a):
        print('Triangle with sides:',a,b,c,'is isosceles triangle (равнобедренный)')
    else:
        print('Triangle with sides:',a,b,c,'is scalene triangle (разностронний)')
