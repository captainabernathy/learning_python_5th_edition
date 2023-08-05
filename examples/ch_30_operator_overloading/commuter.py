# usage: python(2/3) commuter.py

from __future__ import print_function  # for 2.X/3.X interoperability


# NOTE: defining __add__() and __radd__() facilitates communitative addition
class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val


class Commuter2:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self.__add__(other)  # call __add__() explicitly


class Commuter3:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self + other  # swap order and readd... 'self +' calls __add__()


class Commuter4:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    __radd__ = __add__  # alias: cut out the middleman


class Commuter5:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter5):  # type test to avoid object nesting
            other = other.val
        return Commuter5(self.val + other)  # result is another Commuter

    def __radd__(self, other):
        return Commuter5(other + self.val)

    def __str__(self):
        return '<Commuter5: %s>' % self.val


if __name__ == '__main__':
    print('code snippets from pages 946-949\n')

    for klass in (Commuter1, Commuter2, Commuter3, Commuter4, Commuter5):
        print('-' * 60)
        x = klass(88)
        y = klass(99)
        print(x + 1)
        print(1 + y)
        print(x + y)
