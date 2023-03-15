if __name__ == '__main__':
    print('code snippets from pages 411-412\n')
    T = [(1, 2), (3, 4), (5, 6)]  # a list of tuples
    print(T)  # [(1, 2), (3, 4), (5, 6)]
    for (a, b) in T:
        print(a, b)  # 1 2, 3 4, 5 6
    print('')

    D = {'a': 1, 'b': 2, 'c': 3}
    # iterate over dictionary by key and use iterator variable to index into
    # dictionary
    for key in D:
        print(key, '=>', D[key])  # a => 1, b => 2, c => 3
    print('')

    # NOTE: a dictionary's item() method returns a dictionary's elements as
    # a collection of (key,value) tuples... use the list() constructor to
    # build a list of tuples from a dict_items object
    print(list(D.items()))
    print('')

    # use a tuple to iterate over a dict_items object
    for (key, value) in D.items():  # iterate over both keys and values
        print(key, '=>', value)  # a => 1, b => 2, c => 3
    print('')

    for both in T:
        a, b = both  # extract each element of the tuple
        print(a, b)  # 1 2, 3 4, 5 6
    print('')

    ((a, b), c) = ((1, 2), 3)
    print(a, b, c)  # 1 2 3
    print('')

    # iterate over nested sequence
    for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
        print(a, b, c)  # 1 2 3, 4 5 6
    print('')

    for ((a, b), c) in [([1, 2], 3), ['XY', 6]]:
        print(a, b, c)  # 1 2 3, X Y 6
