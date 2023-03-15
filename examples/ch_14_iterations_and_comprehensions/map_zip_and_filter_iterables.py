if __name__ == '__main__':
    print('code snippets from pages 453-454\n')
    # NOTE: the map(), zip(), and filter() constructors return an iterable
    # object that is itself its own iterator... additionally, these objects
    # can only be iterated over once

    # map the absolute value function to each integer between -1 and 1,
    # inclusive
    M = map(abs, (-1, 0, 1))
    print(M)  # <map object...>
    print('')
    
    print(next(M))  # 1

    try:
        while True:
            print(next(M))
    except StopIteration:
        pass
    print('')

    for x in M:  # nothing... map iterator is empty
        print(x)  # loop body never executes
    print('')

    print(list(map(abs, range(-1, 2, 1))))  # [1,0,1]
    print('')

    Z = zip((1, 2, 3), (10, 20, 30))
    print(Z)  # <zip object...>
    print('')

    for pair in Z:  # automatic iteration
        print(pair)  # (1,10), (2,20), (3,30)
    print('')

    # print(next(Z))  # iterator exhausted
    Z = zip((1, 2, 3), (10, 20, 30))

    try:
        while True:
            print(next(Z))
    except StopIteration:
        pass
    print('')

    # NOTE: the filter() constructor applies a function to a iterable object
    # and returns an iterable object for which the function returned True
    print(list(filter(bool, ['spam', '', 'ni'])))  # ['spam', 'ni']
    print('')

    # analogously...
    print([x for x in ['spam', '', 'ni'] if bool(x)])
