# usage: python3 range_iterable.py

if __name__ == '__main__':
    print('code snippets from pages 452-453\n')

    R = range(10)  # build a range object
    print(R)  # range(0,10)

    It = iter(R)
    print(next(It))  # 0
    print(next(It))  # 1
    print(next(It))  # 2
    print('')

    # use the list() constructor to convert a range object to a list
    print(list(range(10)))
    print('')

    # NOTE: range object support the len() function and subscripting, but
    # do NOT support any other sequence operations
    print(len(R))  # 10
    print(R[0])  # 0
    print(R[-1])  # 9
    print('')

    print(next(It))  # 3
    print(It.__next__())  # 4
