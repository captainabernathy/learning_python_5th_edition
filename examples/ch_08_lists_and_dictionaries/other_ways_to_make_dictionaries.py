if __name__ == '__main__':
    print('code snippets from pages 271-272\n')
    # build dictionary using literals
    D1 = {'name': 'Bob', 'age': 40}
    print(D1)
    print('')

    D2 = {}  # empty dictionary
    # populate dictionary using dynamic assignments
    D2['name'] = 'Bob'
    D2['age'] = 40
    print(D2)
    print('')

    # build dictionary using constructor
    # NOTE: a dictionary's keys are provided as keywords to its constructor
    D3 = dict(name='Bob', age=40)  # constructor
    print(D3)
    print('')

    # build a dictionary using a list of tuples where the first element of each
    # tuple in the list represents a key and the second value in the tuple
    # represents a value
    D4 = dict([('name', 'Bob'), ('age', 40)])
    print(D4)
    print('')

    # use the dictionary class's fromkeys() function to build a dictionary from
    # a list of keys
    print(dict.fromkeys(['a', 'b'], 0))
