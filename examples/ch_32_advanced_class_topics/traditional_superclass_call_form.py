from __future__ import print_function


class C:
    def act(self):
        print('spam')


# D is a C, and D overrides C's act() method
class D(C):
    def act(self):
        # explicitly call super class's method passing along a reference to
        # this D... same behavior in 2.X and 3.X
        C.act(self)
        print('eggs')


if __name__ == '__main__':
    print('code snippets from page 1078\n')

    X = D()
    X.act()  # spam, eggs
