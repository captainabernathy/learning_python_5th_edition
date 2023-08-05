# usage: python3 using_dictionaries_to_simulate_flexible_lists.py

if __name__ == '__main__':
    print('code snippets from pages 267-268\n')

    D = {}  # empty dictionary
    D[99] = 'spam'  # assign value to key 99
    print(D)
    print(D[99])  # spam
    print('')

    # keys as integers
    table = {1975: 'Holy Grail',
             1979: 'Life of Brian',
             1983: 'The Meaning of Life'}
    print(table)
    print(table[1975])  # value at 1975
    print(list(table.items()))  # list of key/value tuples
