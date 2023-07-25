import sys


if __name__ == '__main__':
    print('code snippets from page 1053\n')

    sys.path.append('../ch_31_designing_with_classes')
    from listtree import ListTree

    class C(ListTree):
        pass  # OK no __slots__

    X = C()
    print(X)
    print('-' * 80)

    class C(ListTree):
        __slots__ = ['a', 'b']

    X = C()
    X.c = 3
    print(X)  # displays c at X, a and b at C
    print('-' * 80)

    # any non-slot class like ListTree generates an instance of __dict__ and,
    # thus, can safely assume its presence
    class A:
        __slots__ = ['a']

    class B(A, ListTree):
        pass

    X = B()
    print(X)  # has a __dict__ since ListTree does not have __slots__
    print('-' * 80)

    class A:
        __slots__ = ['a']

    class B(A, ListTree):
        __slots__ = ['b']

    X = B()  # has a __dict__ since ListTree does not have __slots__
    print(X)
    print('-' * 80)
