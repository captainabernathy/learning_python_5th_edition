# usage: python(2/3) use_differs_in_python2x_verbose_calls.py

from __future__ import print_function

# NOTE: to use super() with a new-style class in python 2X, you must
# pass super() both the immediate class name (most likely "this class")
# AND (forward) the reference to self


# a new-style class that class that provides a single method act()
class C(object):
    def act(self):
        print('spam')


# NOTE: to maintain interoperability with python 2.X it is OK to call super()
# using the 2.X form, which requires passing both the immediate class and
# self in the call
class D1(C):
    def act(self):
        super(D1, self).act()  # works in 2.X and 3.X
        print('eggs')


class D2(C):
    def act(self):
        try:
            super().act()  # fails in 2.X
            print('eggs')
        except TypeError as ex:
            print(ex)


# NOTE: forwarding self as an argument to a superclass method works the same
# in both 2.X and 3.X
class D3(C):
    def act(self):
        C.act(self)  # works in 2.X and 3.X
        print('eggs')


if __name__ == '__main__':
    print('code snippets from page 1084\n')

    X = D1()
    X.act()  # spam, eggs... in 2.X and 3.X,
    print('')

    X = D2()
    # spam, eggs... 3.X
    # super() takes at least 1 argument (0 given)... in 2.X
    X.act()  # error in 2.X
    print('')

    X = D3()
    X.act()  # spam, eggs... in 2.X and 3.X
