# usage: python3 basic_dictionary_operations.py

if __name__ == '__main__':
    print('code snippets from pages 261-262\n')

    # create a dictionary using key:value pairs
    D = {'spam': 2, 'ham': 1, 'eggs': 3}
    print(D)  # unorder
    print(D['spam'])  # get value/index by key... 2
    print(len(D))  # 3
    # use in to test if a dictionary contains a key
    print('ham' in D)  # key membership

    # NOTE: a dictionary's keys() method returns an iterable keys object
    print(list(D.keys()))  # create list from D's keys

    # same as ^^^
    print([x for x in D.keys()])
