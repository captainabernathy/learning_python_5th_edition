if __name__ == '__main__':
    print('code snippets from pages 119-121\n')
    D = {'a': 1, 'b': 2, 'c': 3}
    print(D)  # {'a': 1, 'b': 2, 'c': 3}

    # add element to dictionary
    D['e'] = 99
    print(D)  # {'a': 1, 'b': 2, 'c': 3, 'e': 99}

    # membership test
    print('f' in D)  # False

    # test for key in dictionary
    if 'f' not in D:
        print('missing')

    if 'f' not in D:
        print('missing')
        print('no, really...')

    # index with default
    # get() method gets the value associated with a key or a default value if
    # the key doesn't exist
    val = D.get('x', 0)
    print(val)

    # ^^^ is the same as
    val = D['x'] if 'x' in D else 0
    print(val)
