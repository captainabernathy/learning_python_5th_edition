from squares_yield import Squares as SquaresYield
from squares_manual import Squares as SquaresManual
from squares_nonyield import Squares as SquaresNonyield
from skipper_yield import SkipObject


# generator function that yields the sequence of squares from 1 to x inclusive
def gen(x):
    for i in range(x):
        yield (i + 1) ** 2


if __name__ == '__main__':
    print('code snippets from pages 930-935\n')
    G = gen(5)  # create a generator... with __iter__() and __next__()
    print(G.__iter__() == G)  # True... both methods exist on the same object

    It = iter(G)  # runs __iter__(): generator returns itself
    print(next(It), next(It))  # 1 4

    # Iteration contexts automatically run iter() and next()
    print(list(gen(5)))  # 1 4 9 16 25
    print('')

    for i in SquaresYield(1, 5):
        print(i, end=' ')  # 1 4 9 16 25
    print('\n')

    S = SquaresYield(1, 5)
    It = S.__iter__()
    print(It.__next__())  # 1
    print(It.__next__())  # 4
    print(It.__next__())  # 9
    print(It.__next__())  # 16
    print(It.__next__())  # 25
    try:
        print(It.__next__())  # whoops...
    except StopIteration:
        print('StopIteration')
    print('')

    S = SquaresYield(1, 5)
    It = iter(S)
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

    for i in SquaresManual(1, 5).gen():
        print(i, end=' ')  # 1 4 9 16 25
    print('\n')

    S = SquaresManual(1, 5)
    It = iter(S.gen())
    print(next(It))  # 1
    print(next(It))  # 4
    print(next(It))  # 9
    print(next(It))  # 16
    print(next(It))  # 25
    try:
        print(next(It))
    except StopIteration:
        print('StopIteration')
    print('')

    # Multiple iterators with yield
    S = SquaresYield(1, 5)
    It = iter(S)
    print(next(It), next(It))  # 1 4

    J = iter(S)
    print(next(J))  # 1...  multiple iterators automatic with yield
    print(next(It))  # 9
    print('')

    # implict calls to __iter__() in iteration contexts make new generators
    # supporting new independent scans
    S = SquaresYield(1, 3)
    for i in S:
        for j in S:
            # 1:1 1:4 1:9 4:1 4:4 4:9 9:1 9:4 9:9
            print('%s:%s' % (i, j), end=' ')
    print('\n')

    for i in SquaresNonyield(1, 5):
        print(i, end=' ')
    print('\n')

    S = SquaresNonyield(1, 5)
    It = iter(S)
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

    # multiple iterators without yield
    It = iter(S)
    print(next(It), next(It))  # 1 4
    J = iter(S)
    print(next(J))  # 1
    print('')

    S = SquaresNonyield(1, 3)
    for i in S:  # each for calls __iter__()
        for j in S:
            # 1:1 1:4 1:9 4:1 4:4 4:9 9:1 9:4 9:9
            print('%s:%s' % (i, j), end=' ')
    print('\n')

    skipper = SkipObject('abcdef')
    It = iter(skipper)
    print(next(It), next(It), next(It))  # a c e
    print('')

    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')  # aa ac ae ca cc ce ea ec ee
    print('')
