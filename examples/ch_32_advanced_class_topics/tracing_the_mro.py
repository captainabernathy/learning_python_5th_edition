# usage: python(2/3) tracing_the_mro.py

from __future__ import print_function


# diamond class hierarchy
#   A
#  / \
# B   C
# \  /
#  D
class A(object):
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


# normal non diamond class hierarchy
#   A2
#  /
# B2  C2
#  \  /
#   D2
class A2(object):
    pass


class B2(A2):
    pass


class C2(object):
    pass


class D2(B2, C2):
    pass


#    A3
#      \
# B3  C3
#  \  /
#   D3
class A3(object):
    pass


class B3(object):
    pass


class C3(A3):
    pass


class D3(B3, C3):
    pass


# new style mro ensures that object is visited last
#  X   Y
#  |   |
# A4   B4
#  \   /
#   D4
class X(object):
    pass


class Y(object):
    pass


class A4(X):
    pass


class B4(Y):
    pass


class D4(A4, B4):
    pass


if __name__ == '__main__':
    print('code snippets from pages 1037-1039\n')

    # __mro__ attribute is a tuple
    # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
    #  <class '__main__.A'>, <type 'object'>)
    print(D.__mro__)  # D, B, C, A, object
    print('')

    # (<class '__main__.D2'>, <class '__main__.B2'>, <class '__main__.A2'>,
    #  <type 'object'>, <class __main__.C2 <class 'object'>)
    print(D2.__mro__)  # D2, B2, A2, C2, object
    print('')

    # (<class '__main__.D3'>, <class '__main__.B3'>, <class '__main__.C3'>,
    #  <class '__main__.A3'>, <class 'object'>)
    print(D3.__mro__)  # B3, C3, A3, object
    print('')

    print(A3.__bases__)  # (<class 'object'>,)
    print(B3.__bases__)  # (<class 'object'>,)

    # (<class '__main__.A3'>,)
    print(C3.__bases__)  # A3

    # (<class '__main__.B3'>, <class '__main__.C3'>)
    print(D3.__bases__)  # B3, C3
    print('')

    # mro() method... returns a list
    # [<class '__main__.D4'>, <class '__main__.A4'>, <class '__main__.X'>,
    #  <class '__main__.B4'>, <class '__main__.Y'>, <class 'object'>]
    print(D4.mro())  # A4, X, B4, Y, object
    print('')

    print(X.__bases__, Y.__bases__)  # (<class 'object'>,) (<class 'object'>,)
    
    # (<class '__main__.X'>,) (<class '__main__.Y'>,)
    print(A4.__bases__, B4.__bases__)  # X, Y
    print('')

    print(D4.mro() == list(D4.__mro__))  # True
    print('')

    # ['D4','A4,'X','B4','Y','object']
    print([cls.__name__ for cls in D4.__mro__])
