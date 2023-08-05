# usage: python(2/3) proxy_coding_requirements.py

from __future__ import print_function


class C(object):
    data = 'spam'

    def __getattr__(self, name):
        print('getattr: ' + name)
        return getattr(self.data, name)


# NOTE: to code a proxy of an object whose interface may in part be invoked by
# built-in operations, new-style classes require both __getattr__() for
# normal names as well as method redefinitions for all names accessed by
# built-in operations -- whether coded manually, obtained from superclasses, or
# generated by tools
class D(object):
    data = 'spam'

    def __getattr__(self, name):  # catch normal names
        print('getattr: ' + name)
        return getattr(self.data, name)

    # redefine built-ins
    def __getitem__(self, i):
        print('getitem: ' + str(i))
        return self.data[i]

    def __add__(self, other):  # run expr on getattr
        print('add: ' + other)
        return getattr(self.data, '__add__')(other)


if __name__ == '__main__':
    print('code snippets from pages 1024-1026\n')

    X = C()
    Y = D()

    # NOTE: __getattr__() intercepts direct method calls in new style classes
    print(X.__getitem__(1))  # getattr: __getitem__, p... 2x and 3x

    # direct call to overloaded __getitem__() method
    print(Y.__getitem__(1))  # getitem: 1, p... 2x and 3x
    print('')

    try:
        # NOTE: since class C does not overload the __getitem__() operator...
        # X is of type C, the operation X[1] results in a TypeError
        print(X[1])
    except TypeError as ex:
        print(ex)  # 'C' object is not subscriptable... 2X and 3X

    print(Y[1])  # getitem: 1, p... 2x and 3x
    print('')

    try:
        # NOTE: since class C does not provide a __getitem__() method, such
        # a call from the calss cannot be applied to an instance
        print(type(X).__getitem__(X, 1))
    except AttributeError as ex:
        # type object 'C' has no attribute '__getitem__'... 2X and 3X
        print(ex)

    print(type(Y).__getitem__(Y, 1))  # getitem: 1, p... 2x and 3x
    print('')

    try:
        # same error as above
        print(C.__getitem__(X, 1))
    except AttributeError as ex:
        # type object 'C' has no attribute '__getitem__'... 2X and 3X
        print(ex)

    print(D.__getitem__(Y, 1))  # getitem: 1, p... 2x and 3x
    print('')

    # __getattr__() intercepts direct method call
    print(X.__add__('eggs'))  # getattr: __add__, spameggs... 2X and 3X

    # direct call to overloaded __add__() method
    print(Y.__add__('eggs'))  # add: eggs spameggs in 2x and 3x
    print('')

    try:
        # fails for the same rease as X[1]
        print(X + 'eggs')
    except TypeError as ex:
        # unsupported operand type(s) for +: 'C' and 'str'... 2X and 3X
        print(ex)

    print(Y + 'eggs')  # add: eggs, spameggs... 2X and 3X
    print('')

    try:
        # fails for the same reason as __getitem__() did above
        print(type(X).__add__(X, 'eggs'))
    except AttributeError as ex:
        print(ex)

    print(type(Y).__add__(Y, 'eggs'))  # add: eggs, spameggs... 2X and 3X
    print('')

    try:
        # same error as above
        print(C.__add__(X, 'eggs'))
    except AttributeError as ex:
        print(ex)

    print(D.__add__(Y, 'eggs'))  # add: eggs, spameggs... 2X and 3X
    print('')

    # __getattr__() intercepts named method call
    # getattr: upper, <built-in method of str object at 0x...>... 2X and 3X
    print(X.upper)
    print(Y.upper)
    print('')

    # getattr: upper, SPAM... 2X and 3X
    print(X.upper())
    print(Y.upper())
    print('')

    
