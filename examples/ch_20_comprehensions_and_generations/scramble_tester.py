# usage: python3 scramble_tester.py

# program uses scramble module to test the intersect() and union() functions
# of the module inter2
from scramble import scramble
from inter2 import intersect
from inter2 import union


# this function tests the function passed to func on the collection of items
# passed to items by successively reordering the elements contained in items
# such that the first element in items is moved to the end for each element in
# items and calling func on each of the reorderings
# when trace is True, the arguments that will be passed to func are printed
# before the call
def tester(func, items, trace=True):
    for args in scramble(items):  # generate cyclic permutation
        if trace:
            print(args)
        print(sorted(func(*args)))


if __name__ == '__main__':
    print('code snippets from page 635\n')

    # set intersection
    tester(intersect, ('aab', 'abcde', 'ababab'))
    print('')

    # set intersection
    tester(intersect, ([1, 2], [2, 3, 4], [1, 5, 2, 7, 3]), False)
    print('')

    # set union
    tester(union, ('aab', 'abcde', 'ababab'))
    print('')

    # set union
    tester(union, ([1, 2], [2, 3, 4], [1, 5, 2, 7, 3]), False)
    print('')
