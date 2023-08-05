# usage: python3 mapattrs_slots.py

from mapattrs import mapattrs
from mapattrs import trace


class A(object):
    __slots__ = ['a', 'b']
    x = 1
    y = 2


class B(A):
    __slots__ = ['b', 'c']


class C(A):
    x = 2


class D(B, C):
    z = 3

    def __init__(self):
        self.name = 'Bob'


if __name__ == '__main__':
    print('code snippets from page 1044\n')

    It = D()
    trace(mapattrs(It, bysource=True))
