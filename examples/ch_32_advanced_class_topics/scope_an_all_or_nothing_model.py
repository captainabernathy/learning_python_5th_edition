class B1:
    def __init__(self):
        print('B1.__init__')
        super().__init__()


class C1:
    def __init__(self):
        print('C1.__init__')
        super().__init__()


class D1(B1, C1):
    def __init__(self):
        print('D1.__init__')
        super().__init__()


# what if you must use a class that doesn't call super?
# NOTE: when propagation requirements are not satisfied, it breaks the
# chain of propagation
class B2:
    def __init__(self):
        print('B2.__init__')


class C2:
    def __init__(self):
        print('C2.__init__')
        super().__init__()


# NOTE: even though C2 calls super(), since B2 does not, and B2 is first in
# D2's mro, C2 is never instantiated bc B2 breaks the chain of propagation
class D2(B2, C2):
    def __init__(self):
        print('D2.__init__')
        super().__init__()


if __name__ == '__main__':
    print('code snippets from pages 1090-1091\n')

    X = D1()  # D1.__init__, B1.__init__, C1.__init__
    print('')

    # (<class, '__main__.D1'>,<class '__main__.B1'>,<class '__main__.C1'>,
    #  <class 'object'>)
    print(D1.__mro__)
    print('')

    # D2.__init__ B2.__init__... since B2 doesn't call super(), C2 is never
    # instantiated
    X = D2()
    print('')
