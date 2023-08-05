# usage: python2 boolean_methods_in_2x.py

from __future__ import print_function


# NOTE: in python 2.X, __bool__() is ignorned bc an object is always considered
# True by default
# in python2.X use the __nonzero__() method for boolean values
# in python 3.X __nonzero__() is ignored, and an object is considered True by
# default

class C1:
    def __bool__(self):
        print('in bool')
        return False


class C2:
    def __nonzero__(self):  # works in 2x only
        print('in nonzero')
        return False


if __name__ == '__main__':
    print('code snippets from pages 957-958\n')

    X = C1()
    print(bool(X))  # True... 2.X ignores __bool__()
    print('')

    if X:  # object vacuously true in 2.X (object is nonzero)
        print(99)  # 99... 2.X
    print('')

    X = C2()
    print(bool(X))  # in nonzero False... 2.X
    if X:
        print(99)  # in nonzero... 2.X
