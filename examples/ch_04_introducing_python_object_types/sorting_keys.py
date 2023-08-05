# usage: python3 sorting_keys.py

if __name__ == '__main__':
    print('code snippets from pages 121-122\n')

    D = {'a': 1, 'b': 2, 'c': 3}
    print(D)  # {'a': 1, 'b': 2, 'c': 3}

    # get an unordered list of keys
    Ks = list(D.keys())
    print(Ks)  # ['a','b','c']

    # sort keys
    Ks.sort()
    print(Ks)  # ['a','b','c']

    # iterate over sorted keys
    for key in Ks:
        print(key, '=>', D[key])
    print('')

    # alternatively use the sorted() function
    for key in sorted(D):
        print(key, '=>', D[key])
    print('')

    # iterate over each character in 'spam'
    for c in 'spam':
        print(c.upper())
    print('')

    # while loop example
    x = 4
    while x > 0:
        print('spam!' * x)
        x -= 1
