import sys


def func(a, b, c, e=True, f=None):
    x = 1
    y = 2


def catcher(*pargs, **kargs):
    print('%s, %s' % (pargs, kargs))


def f1(*kargs, **pargs):
    pass


def f2(a, b, *kargs, **pargs):
    pass


if __name__ == '__main__':
    # NOTE: the fn_name.__code__ attribute is named fn_name.func_code in
    # python <= 2.5
    code = func.__code__ if sys.version_info[0] == 3 else func.func_code

    print(code)  # <code object func at 0x, file "/path", line 1>
    print('')

    # total number of local variables
    print(code.co_nlocals)  # 7

    # all local variables
    print(code.co_varnames)  # ('a','b','c','e','f','x','y')

    # the first N locals are the expected arguments
    print(code.co_varnames[:code.co_argcount])  # ('a','b','c','e','f')
    print('')

    catcher(1, 2, 3, 4, 5)  # (1,2,3,4,5), {}
    print('')

    catcher(1, 2, c=3, d=4, e=5)  # (1,2), {'c':3,'d':4,'e':5}
    print('')

    # NOTE: arg[0] is major release version... format (N1,N2,N3,'string',N4)
    print(tuple(sys.version_info))  # ie: (2,7,18,'final',0)
    print('')

    # NOTE: starred arguments show up as locals but not expected arguments...
    # this makes validating extra positional arguments difficult
    code = f1.__code__
    print(code.co_nlocals, code.co_varnames)  # 2 ('kargs','pargs')
    print(code.co_argcount, code.co_varnames[:code.co_argcount])  # 0 ()
    print('')

    code = f2.__code__
    print(code.co_nlocals, code.co_varnames)  # 4 ('a','b','kargs','pargs')
    print(code.co_argcount, code.co_varnames[:code.co_argcount])  # 2 ('a','b')
