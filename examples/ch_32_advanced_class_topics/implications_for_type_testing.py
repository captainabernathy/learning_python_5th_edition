# usage: python(2/3) implications_for_type_testing.py

from __future__ import print_function


# old style class in 2X, new style class in 3X
class C:
    pass


# old style class in 2X, new style class in 3X
class D:
    pass


# new style class in 2X and 3X
class NC(object):
    pass


# new style class in 2X and 3X
class ND(object):
    pass


if __name__ == '__main__':
    print('code snippets from pages 1029-1030\n')

    c, d = C(), D()

    # True in 2X... both c and d's type is instance
    # False in 3X... bc 3X compares the instances' classes... c's type is C and
    # d's type is D
    print(type(c) == type(d))
    print('')

    # <type 'instance'> <type 'instance'>... 2X
    # <class '__main__.C'> <class '__main__.D'>... 3X
    print(type(c), type(d))
    print('')

    c1, c2 = C(), C()
    # True... 2X (both types are instance) and 3X (both types are C)
    print(type(c1) == type(c2))
    print('')

    # False... 2X and 3X... c's class is C and d's class is D in both
    print(c.__class__ == d.__class__)
    print('')

    # __main__.C __main__.D... 2X
    # <class '__main__.C> <class '__main__.D'>... 3X
    print(c.__class__, d.__class__)
    print('')

    # NOTE: new style classes are treated similarly in both
    nc, nd = NC(), ND()
    # False... 2X and 3X
    print(type(nc) == type(nd))
    print('')

    # <class '__main__.NC'> <class '__main__.ND'>... 2X and 3X
    print(type(nc), type(nd))
    print('')

    # __main__.C __main__.D... 2X
    # <class '__main__.C'> <class '__main__.D'>
    print(c.__class__, d.__class__)
