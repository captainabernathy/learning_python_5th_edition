# usage: python3 dictionary_comprehensions_in_3x_and_27.py

if __name__ == '__main__':
    print('code snippets from pages 274-275\n')

    # the zip() function can be used to construct a list of tuples or a
    # dictionary from a list of keys and values
    D1 = list(zip(['a', 'b', 'c'], [1, 2, 3]))  # zip together keys and values
    print(D1)  # a list of tuples
    print('')

    D2 = dict(zip(['a', 'b', 'c'], [1, 2, 3]))  # dictionary from zip results
    print(D2)  # a dictionary of key value pairs
    print('')

    # dictionary comprehension...
    D3 = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
    print(D3)
    print('')

    # dictionary of squares
    D4 = {x: x ** 2 for x in [1, 2, 3, 4]}
    print(D4)
    print('')

    D5 = {c: c * 4 for c in 'SPAM'}
    print(D5)
    print('')

    D6 = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
    print(D6)
    print('')

    D7 = dict.fromkeys(['a', 'b', 'c'])  # initialize dict from keys
    print(D7)  # dictionary contains keys but their values are None
    print('')

    D8 = {k: None for k in ['a', 'b', 'c']}  # same as ^^^
    print(D8)
    print('')

    D9 = dict.fromkeys('spam')  # initialize with None for values
    print(D9)  # each letter in 'spam' is a key
    print('')

    D10 = {k: None for k in 'spam'}  # same as ^^^
    print(D10)
