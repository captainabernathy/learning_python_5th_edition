# NOTE: classes that use __slots__ do NOT have a __dict__ attribute by default
class C:  # Note (object) required in 2x
    __slots__ = ['a', 'b']


# class D:
#     __slots__ = ['a', 'b']
#     def __init__(self):
#         self.d = 4  # can't do this... no new names if no __dict__!!!


# work-around for ^^^... include __dict__ in __slots__ explicitly to create an
# attribute namespace dictionary
class D:
    __slots__ = ['a', 'b', '__dict__']
    c = 3  # class attributes are ok

    def __init__(self):
        self.d = 4  # d stored in __dict__


if __name__ == '__main__':
    print('code snippets from pages 1047-1048\n')

    X = C()
    X.a = 1
    print(X.a)  # 1

    try:
        print(X.__dict__)  # doesn't exits with classes that only have slots
    except AttributeError as ex:
        print(ex)  # 'C' object has no attribute '__dict__'
    print('')

    # getattr() and setattar() are storage neutral
    print(getattr(X, 'a'))  # 1

    setattr(X, 'b', 2)
    print(X.b)  # 2
    print('')

    # dir() collects all inherited names... __slots__ included
    print('a' in dir(X))  # True
    print('b' in dir(X))  # True
    print('')

    X = D()
    print(X.d)  # 4
    print(X.c)  # 3

    try:
        print(X.a)  # a not initialized
    except AttributeError as ex:
        print('Error: ', ex)  # Error: 'D' object has no attribute 'a'
    print('')

    X.a = 1
    X.b = 2
    print(X.__dict__)  # {'d': 4}
    print(X.__slots__)  # ['a', 'b', '__dict__']
    print('')

    print(getattr(X, 'a'), getattr(X, 'c'), getattr(X, 'd'))  # 1 3 4

