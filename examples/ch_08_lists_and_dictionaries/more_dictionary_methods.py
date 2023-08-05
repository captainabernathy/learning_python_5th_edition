# usage: python3 more_dictionary_methods.py

if __name__ == '__main__':
    print('code snippets from pages 263-264\n')

    D = {'spam': 2, 'ham': 1, 'eggs': 3}
    print(D)

    # a dictionary's values() methods returns an iterable containing the values
    # associated with the keys in this dictionary
    print(list(D.values()))  # get list values

    # a dictionary's items() method returns an iterable containing the entries
    # (key/value pairs) in this diectionary
    print(list(D.items()))  # get keys and values in list of tuples

    # NOTE: a dictionary's get() method returns the value in this dictionary
    # that is associated with the key provided
    print(D.get('spam'))  # get value at key... 2

    # if a key provided to a dictionary's get() method does not exist in this
    # dictionary, the method will return None
    print(D.get('toast'))  # None

    # optionally, a dictionary's get() method can retrun a default value when
    # the key provided does not exist in this dictionary
    print(D.get('toast', 88))  # returns 88... since 'toast' is not a key in D
    print(D)
    print('')

    D2 = {'toast': 4, 'muffin': 5}
    print(D2)

    # a dictionary's update() method can be used to concatenate the provided
    # dictionary to this dictionary
    D.update(D2)  # adds D2 to D
    print(D)
    print('')

    # a dictionary's pop() method removes the entry associated with the key
    # provided in this dictionary and return value associated with the key
    print(D.pop('muffin'))  # delete by key and return value
    print(D)
    print(D.pop('toast'))
    print(D)
    print('')

    L = ['aa', 'bb', 'cc', 'dd']
    print(L)
    print(L.pop())  # delete and return last element
    print(L)
    print(L.pop(1))  # delete and return element at position
    print(L)
