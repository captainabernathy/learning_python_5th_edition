if __name__ == '__main__':
    print('code snippets from pages 131-132\n')
    print(1 > 2, 1 < 2)  # False True
    print(bool('spam'))  # True

    # None is a place holder object
    X = None
    print(X)  # None
    print(bool(X))  # False

    # initialize a lsit of 100 Nones
    L = [None] * 100
    print(L)  # [None,...,None]
    print('')

    print(type(L))  # <class 'list'> in 3.x, <type 'list'> in 2.x
    print(type(type(L)))  # <class 'type'> in 3.x, <type, type> in 2.x

    # NOTE: use isinstance() to compare types
    if type(L) == type([]):  # makes flake8 complain
        print('yes')

    if type(L) == list:  # does not make flake8 complain
        print('yes')

    if isinstance(L, list):  # preferred way to test types
        print('yes')
