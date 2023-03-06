if __name__ == '__main__':
    print('code snippets from pages 266-267\n')
    table = {'Holy Grail': '1975',
             'Life of Brian': '1979',
             'The Meaning of Life': '1983'}
    print(table)
    print('')

    print(list(table.items()))  # list of tuples
    print('')

    # print the list of movie titles (keys) from the dictionary that have an
    # an associated value of '1975'
    print([title for (title, year) in table.items() if year == '1975'])
    print('')

    K = 'Holy Grail'
    print(table[K])  # 1975... the value at key K

    V = '1975'
    print([key for (key, value) in table.items() if value == V])
    print([key for key in table.keys() if table[key] == V])  # same as ^^^
