# usage: python(2/3) implications_for_attribute_interception.py

# In 2X classes dreived from object are treated as new style classes if no
# other built-in type is appropriate to use
from __future__ import print_function


# NOTE: in python 2X, built-in operations -- such as indexing (__getitem__())
# and print (__str__()) operations -- are routed through __getattr__() for
# classic classes (classes that do not explicitly inherit from object)
class Classic:
    data = 'spam'

    def __getattr__(self, name):  # intercepts built-in operations in 2X
        print(name)
        return getattr(self.data, name)


# NOTE: in 3X, all classes implicitly inherit from object, but to create a
# new style class in 2X, it is necessary to explicitly inherit from object
class NewStyle(object):  # New style in 2x and 3x
    data = 'spam'

    # NOTE: built-in operations are NOT routed through __getattr__() in new
    # style classes
    def __getattr__(self, name):
        print(name)
        return getattr(self.data, name)


class ClassicDummy:
    pass


class NewStyleDummy(object):
    pass


# NOTE: with new style classes, __getattr__() intercepts calls to attributes
# accessed by explicit name but NOT attributes fetched by built-in operations
class NewStyleBad(object):
    def __getattr__(self, name):
        print(name)


if __name__ == '__main__':
    print('code snippets from pages 1023-1024\n')

    C = Classic()
    try:
        # C[0] == C.__getitem__(0)
        # intercepted by __getattr__() in  2.X... returns C.data.__getitem__(0)
        print(C[0])  # __getitem__, s... in 2X
    except TypeError as ex:
        print(ex)  # 'Classic' object is not subscriptable... in 3X
    print('')

    # print calls C.__str__()
    #  intercepted by __getattr__() in 2X... returns C.data.__str__()
    # __str__, spam...  in 2X
    # <__main__.Classic object at 0x...>... in 3X
    print(C)
    print('')

    N = NewStyle()

    try:
        # built-ins NOT routed to __getattr__() with new style class
        print(N[0])
    except TypeError as ex:
        print(ex)  # 'NewStyle' object does not support indexing.. in 2X and 3X
    print('')

    print(N)  # <__main__.NewStyle object at 0x...>... in 2X and 3X
    print('')

    CD = ClassicDummy()
    CD.normal = lambda: 99
    print(CD.normal())  # 99... in 2X and 3X

    CD.__add__ = lambda y: (88 + y)
    print(CD.__add__(1))  # 89... in 2X and 3X
    try:
        print(CD + 1)  # 89... via operator overloading... in 2X
    except TypeError as ex:
        # unsupported operand types(s) or +: 'ClassicDummy' and int... in 3X
        print(ex)
    print('')

    ND = NewStyleDummy()
    ND.normal = lambda: 99
    print(ND.normal())  # 99... in 2X and 3X

    ND.__add__ = lambda y: (88 + y)
    print(ND.__add__(1))  # 89 in 2X and 3X
    try:
        print(ND + 1)
    except TypeError as ex:
        # unsupported operand types(s) or +: 'NewStyleDummy' and int...
        # in 2X and 3X
        print(ex)
    print('')

    NB = NewStyleBad()
    # NOTE: __getattr__() runs for named methods in new style classes
    print(NB.normal)  # normal, None... in 2X and 3X
    print('')

    print(NB.__add__)  # __add__, None... in 2X and 3X
    print('')

    try:
        print(NB + 1)
    except TypeError as ex:
        # unsupported operand type(s) for +: 'NewStyleBad' and 'int'... in 2X
        # and 3X
        print(ex)
