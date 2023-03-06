if __name__ == '__main__':
    print('code snippets from page 258\n')
    L = ['spam', 'eggs', 'ham', 'toast']
    print(L)  # ['spam', 'eggs', 'ham', 'toast']

    # the del statement can be used to remove an element from a list
    del L[0]  # delete one item
    print(L)  # ['eggs', 'ham', 'toast']

    # delete every element starting a position 1 to the end of the list
    del L[1:]  # delete secion
    print(L)  # ['eggs']
    print('')

    L = ['Already', 'got', 'one']
    print(L)  # ['Already', 'got', 'one']

    # NOTE: assigning an empty list to an index stores a reference to the
    # empty list in the slot... while assigning an empty list to a slice of
    # elements deletes the slice from the list

    L[1:] = []  # delete multiple elements
    print(L)  # ['Already']
    L[0] = []  # stores reference to empty list
    print(L)  # [[]]  list containing an empty list
