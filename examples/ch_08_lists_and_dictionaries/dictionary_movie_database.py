if __name__ == '__main__':
    print('code snippets from page 265\n')
    table = {'1975': 'Holy Grail',
             '1979': 'Life of Brian',
             '1983': 'The Meaning of Life'}
    print(table)

    year = '1983'
    movie = table[year]
    print(movie)
    print('')

    # iterate over keys in dictionary and print the key and the value at it
    for year in table:
        print(year + '\t' + table[year])
