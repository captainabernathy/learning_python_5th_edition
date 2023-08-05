# usage: python3 the_basics_cooperative_super_call_in_action.py

class B1:
    def __init__(self):
        print('B1.__init__')


class C1:
    def __init__(self):
        print('C1.__init__')


# disjoint superclasses... no common explict ancestor between superclasses
class D1(B1, C1):
    pass


class D11(B1, C1):
    def __init__(self):
        B1.__init__(self)  # traditional form... invokes superclasses by name
        C1.__init__(self)


class A2:
    def __init__(self):
        print('A2.__init__')


class B2(A2):
    def __init__(self):
        print('B2.__init__')
        A2.__init__(self)


class C2(A2):
    def __init__(self):
        print('C2.__init__')
        A2.__init__(self)


# diamond... calls B2.__init__() upon instantiation
class D2(B2, C2):
    pass


# another diamond
class D22(B2, C2):
    def __init__(self):
        B2.__init__(self)  # traditional form... BUT...
        C2.__init__(self)  # A gets initialized twice!!!


class A3:
    def __init__(self):
        print('A3.__init__')


class B3(A3):
    def __init__(self):
        print('B3.__init__')
        super().__init__()  # propagates call through the tree


class C3(A3):
    def __init__(self):
        print('C3.__init__')
        super().__init__()  # propagates call through the tree


# NOTE: if all classes use super -- or are appropriately coerced by proxies to
# behave as if they do -- method calsses are dispached according to class order
# in the MRO such that the top-level class's method runs only once
class D3(B3, C3):
    pass  # mro => B3.__init__, C3.__init__, A3.__init__


if __name__ == '__main__':
    print('code snippets from pages 1087-1088\n')

    # D1 is a (B1, C1)
    x = D1()  # B1.__init__
    print('')

    x = D11()  # B1.__init__, C1.__init__
    print('')

    x = B2()  # B2.__init__, A2.__init__... each super works by itself
    print('')

    x = C2()  # C2.__init__, A2.__init__
    print('')

    x = D2()  # B2.__init__, A2.__init__... runs left most first
    print('')

    # initializes A2 twice
    x = D22()  # B2.__init__, A2.__init__, C2.__init__, A2.__init__
    print('')

    x = B3()  # B3.__init__(), A3.__init__
    print('')

    x = C3()  # C3.__init__, A3.__init__
    print('')

    x = D3()  # B3.__init__, C3.__init__, A3.__init__
    print('')

    # (<class '__main__.B3'>, <class '__main__.A3'>, <class 'object'>)
    print(B3.__mro__)
    print('')

    # (<class '__main__.D3'>, <class '__main__.B3'>, <class '__main__.C3'>,
    #  <class '__main__.A3'>, <class 'object'>)
    print(D3.__mro__)
