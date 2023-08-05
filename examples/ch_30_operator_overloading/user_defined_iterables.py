# usage: python3 user_defined_iterables.py

from squares import Squares


# generator function that yields the squares of the numbers from start to
# stop + 1
def gsquares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2


if __name__ == '__main__':
    print('code snippets from pages 924-927\n')

    # for loops call iter(), which call __iter__()
    # each iteration calls next(), which calls __next__()
    for i in Squares(1, 5):
        print(i, end=' ')  # 1 4 9 16 25
    print('\n')

    X = Squares(1, 5)
    It = iter(X)  # iter() calls __iter__()
    print(next(It))  # 1
    print(next(It))  # 4
    print(next(It))  # 9
    print(next(It))  # 16
    print(next(It))  # 25
    try:
        print(next(It))  # whoops...
    except StopIteration:
        print('StopIteration')
    print('')

    X = Squares(1, 5)
    try:
        print(X[1])  # whoops... Squares does not implement __getitem__()
    except TypeError:
        print('TypeError')  # object doesn't support indexing
    print('')

    # so you have to coerce it into a list
    print(list(X)[1])  # 2

    # Single vs multiple scans
    X = Squares(1, 5)
    print([n for n in X])  # [1,4,9,16,25]... exhausts items: __iter__()
                           # returns self
    print([n for n in X])  # []... now it's empty: __iter__() returns self
    print([n for n in Squares(1, 5)])  # makes a new iterable object
    print(list(Squares(1, 3)))  # makes a new object for each new call to
                                # __iter__()
    print('')

    # other iteration contexts
    print(36 in Squares(1, 10))  # True
    a, b, c = Squares(1, 3)  # each calls __iter__() and then __next__()
    print(a, b, c)  # 1 4 9
    print(':'.join(map(str, Squares(1, 5))))  # 1:4:9:16:25
    print('')

    X = Squares(1, 5)
    print(tuple(X), tuple(X))  # (1,4,9,16,25) ()...
                               # iterator exhausted in second tuple()
    print('')

    X = list(Squares(1, 5))
    print(tuple(X), tuple(X))  # not exhausted bc X is a list
    print('')

    for i in gsquares(1, 5):
        print(i, end=' ')  # 1 4 9 16 25
    print('\n')

    # same as ^^^
    for i in (x ** 2 for x in range(1, 6)):
        print(i, end=' ')  # 1 4 9 16 25
    print('\n')

    print([x ** 2 for x in range(1, 6)])  # [1,4,9,16,25]... easiest
