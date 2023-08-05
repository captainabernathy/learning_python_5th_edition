# usage: python3 avoiding_missing_key_errors.py

if __name__ == '__main__':
    print('code snippets from page 269\n')

    Matrix = {}  # empty dictionary
    # hypothetical 3D array
    # use keys as coordinates that have some associated value
    Matrix[(2, 3, 4)] = 88
    Matrix[(7, 8, 9)] = 99
    print(Matrix)

    # search for value at (non-existent) key
    if (2, 3, 6) in Matrix:
        print(Matrix[(2, 3, 6)])
    else:
        print(0)
    print('')

    # NOTE: indexing for a non-existent key is a KeyError
    try:
        print(Matrix[(2, 3, 6)])
    except KeyError:
        print(0)
    print('')

    # use dictionary's get() method and provided it with a default argument
    # when searching for a potentially non-existent key
    print(Matrix.get((2, 3, 4), 0))  # 0 if not there
    print(Matrix.get((2, 3, 6), 0))
