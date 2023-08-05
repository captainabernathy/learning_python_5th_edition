# usage: python(2/3) slot_tests.py

from __future__ import print_function
import timeit


if __name__ == '__main__':
    print('code snippets from page 1054\n')

    # basis for both tests
    base = '''
Is = []
for i in range(1000):
    X = C()
    X.a = 1
    X.b = 2
    X.c = 3
    X.d = 4
    t = X.a + X.b + X.c + X.d
    Is.append(X)
    '''

    # C has four slots, base creates an instance C fills its slots, and appends
    # it to a list 1000 times
    stmt = '''
class C:
    __slots__ = ['a', 'b', 'c', 'd']
    ''' + base
    print('Slots   =>', end=' ')
    print(min(timeit.repeat(stmt, number=1000, repeat=3)))
    print('')

    # C is an empty class, base creates an instance of C, adds four attributes
    # to it, and appends it to a list 1000 times
    stmt = '''
class C:
    pass
    ''' + base
    print('Nonslots=>', end=' ')
    print(min(timeit.repeat(stmt, number=1000, repeat=3)))
