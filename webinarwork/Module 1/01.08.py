# # def foo(d, e, f):
# #     print(d, e, f)
# #
# # a, b, c = 1, 2, 3
# #
# # foo(a, b, c)    # Output is 1 2 3
# # foo(b, a, c)
# # foo(c, b, a)
#
# # def foo(arg1=0, arg2=0, arg3=0):
# #     print(arg1, arg2, arg3)
# #
# # a, b, c = 1, 2, 3
# # foo(a,b,c)
# # foo(arg1=a, arg2=b, arg3=c)
# # foo(arg3=c, arg2=b, arg1=a)
# # foo(arg2=b, arg1=a, arg3=c)
#
#
# # def foo(*args):
# #     print(args)
# #
# # a, b, c = 1, 2, 3
# #
# # foo(a, b, c)
# # foo(a, b)
# # foo(a)
# # foo(b, c)
#
#
# # # def foo(**kwargs):
# # #     print(kwargs)
# # a, b, c = 1, 2, 3
# # #
# # # foo(a=1, b=2, c=3)
# # # foo(a=1, b=2)
# # # foo(a=1)
# # # foo(b=2, c=3)
# #
# # def foo(*args):
# #     print(args)
# # foo(a, 2, 3)
#
# # def foo(*args,**kwargs):
# #     print(args, kwargs)
# #
# # a, b, c = 1, 2, 3
# # foo(a=1,)           # () {'a': 1}
# # foo(a=1, b=2, c=3)  # () {'a': 1, 'b': 2, 'c': 3}
# # foo(1, 2, a=1, b=2) # (1, 2) {'a': 1, 'b': 2}
# # foo(1, 2)           # (1, 2) {}
#
# # def foo(var, *args,**kwargs):
# #     print(var, args, kwargs)
# #
# # a, b, c = 1, 2, 3
# #
# # foo(1,a,b,c, a=4,b=5,c=6)
#
#
# # def foo(var, kvar=0, *args,**kwargs):
# #     print(var, kvar, args, kwargs)
# # a, b, c = 1, 2, 3
# #
# #
# # foo(1, a=1,)                # 1 0 () {'a': 1}
# # foo(1, 2, a=1, b=2, c=3)    # 1 0 () {'a': 1, 'b': 2, 'c': 3}
# # foo(1, 2, 3, a=1, b=2)      # 1 2 () {'a': 1, 'b': 2}
# # foo(1, 2, 3, 4, a=1, b=2)   # 1 2 (3,) {'a': 1, 'b': 2}
# # foo(1, kvar=2)              # 1 2 () {}
#
#
# # args = (1, 2, 3, 4)
# # print(*args, sep=', ') # Выводит 1 2 3 4
#
# def foo(a, b=0, *args, **kwargs):
#     print(a, b, args, kwargs)
#
# tup = (1, 2, 3, 4)
# lst = [1, 2, 3, 4]
# d = {'e':1, 'f':2, 'g':'3'}
#
# foo(*lst)
#
# foo(1, *tup)
#
# foo(1, 5, *tup)
#
#
# foo(1, *tup, **d)
#
#
# foo(*tup, **d)
#
# d['b'] = 45
# foo(2, **d)


# def foo(a, *args, b=0):
#     print(a, args, b)
# tup = (1, 2, 3, 4)
#
# foo(*tup, b=35)



# foo(*tup, b=35)         # 1 (2, 3, 4) 35
# foo(1, *tup, b=35)      # 1 (1, 2, 3, 4) 35
# foo(1, 5, *tup, b=35)   # 1 (5, 1, 2, 3, 4) 35


def foo(a, *, b, c):
    print(a, b, c)
tup = (1, 2, 3, 4)
foo(1, b=35, c=55) # 1 35 55
foo(c= 55, b=35, a=1) # 1 35 55
foo(1, 2, 3)
# TypeError: foo() takes 1 positional argument but 3 were given