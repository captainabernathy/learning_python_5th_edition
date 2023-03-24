# program demonstrates usage of the permute1() and permute2() functions
# found in the permute module
from scramble import scramble
from permute import permute1
from permute import permute2

if __name__ == '__main__':
    print('code snippets from pages 635-637\n')
    print(list(scramble('abc')))
    print('')

    print(permute1('abc'))  # returns a list
    print('')

    # list() constructor required to obtain results from generator expression
    print(list(permute2('abc')))
    print('')

    print(list(permute2('spam')))
    print(len(list(permute2('spam'))))  # 24
    print('')

    print(permute1([1, 2, 3]))
    print(list(permute2([1, 2, 3])))
    print('')

    for p in permute1('abc'):
        print(p)
    print('')

    It = permute2('abc')
    # manually iterate over results
    try:
        while True:
            print(next(It))
    except StopIteration:
        pass
