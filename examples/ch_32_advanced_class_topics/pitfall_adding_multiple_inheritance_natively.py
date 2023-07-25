# NOTE: with multiple inheritance, methods invoked through the proxy object
# returned from super() will be routed per MRO order, which, depending on
# where else super() might be used, might invoke a method in a class that is
# not the caller's superclass at all

# A is a class that provides the single method act()
class A:
    def act(self):
        print('A')


# B is also a class that provides the single method act()
class B:
    def act(self):
        print('B')


# C1 is an A that overrides its act() method
class C1(A):
    def act(self):
        super().act()  # super applied to single-inheritance tree


# NOTE: when a mixin class uses super() to call a method, it will call the
# first class to match the method from left to right, regardless
# C2 is an A and a B, and C2 overrides the method act() to call super().act()
# which results in a call to A.act()
class C2(A, B):
    def act(self):
        super().act()  # doesn't fail on multi-inheritance


# C2 is an B and a A, and C2 overrides the method act() to call super().act()
# which results in a call to B.act()
class C3(B, A):
    def act(self):
        super().act()  # if B is listed first, A.act(self) no longer runs


# D provides the methods act() and other()
class D:
    def act(self):
        print('D')

    def other(self):
        D.act(self)  # forwards self to act()


class C4(A, D):
    def act(self):
        super().act()  # calls A's act()

    def other(self):  # calls D's other()
        super().other()


class C5(B, D):
    def __init__(self):
        self.proxy = super()

    def act(self):
        self.proxy.act()  # calls B's act()

    def other(self):
        self.proxy.other()  # calls D's other()


if __name__ == '__main__':
    print('code snippets from pages 1080-1082\n')

    X = C1()  # a C1 is an A
    X.act()  # A
    print('')

    X = C2()  # a C2 is an (A, B)
    X.act()  # A
    print('')

    X = C3()  # a C3 is a (B, A)
    X.act()  # B
    print('')

    X = C4()  # a C4 is an (A, D)
    X.act()  # A
    X.other()  # D
    print('')

    X = C5()  # a C5 is a (B, D)
    X.act()  # B
    X.other()  # D
    print('')

