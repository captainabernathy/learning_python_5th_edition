if __name__ == '__main__':
    print('code snippets from page 263\n')
    D = {'spam': 2, 'ham': 1, 'eggs': 3}
    print(D)

    # change the value at the key ham
    D['ham'] = ['grill', 'bake', 'fry']
    print(D)

    # NOTE: a del statement removes an entry (key:value pair) from a dictionary
    del D['eggs']  # delete entry
    print(D)

    D['brunch'] = 'Bacon'  # add new entry
    print(D)
