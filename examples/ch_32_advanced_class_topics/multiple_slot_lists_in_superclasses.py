# usage: python3 multiple_slot_lists_in_superclasses.py

# NOTE: an instance inherits the union of the slots on its class tree
class E:
    __slots__ = ['c', 'd']


class D(E):
    __slots__ = ['a', '__dict__']


if __name__ == '__main__':
    print('code snippets from page 1049\n')

    X = D()
    X.a = 1
    X.b = 2  # new attribute on the __dict__
    X.c = 3  # inherited from E
    print(X.a, X.b, X.c)  # 1 2 3
    print('')

    print(E.__slots__)  # ['c', 'd']
    print(D.__slots__)  # ['a', '__dict__']
    print(X.__slots__)  # ['a', '__dict__']
    print(X.__dict__)  # {'b': 2}
    print('')

    for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
        print(attr, '=>', getattr(X, attr))  # misses some superclass slots
    print('')

    # dir() includes all slot names
    print(dir(X))  # [..., 'a','b,'c','d']

