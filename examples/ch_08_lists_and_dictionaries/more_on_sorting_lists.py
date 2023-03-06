if __name__ == '__main__':
    print('code snippets from pages 255-256\n')
    # NOTE: capital letters have a lower numeric value than lowercase letters
    L = ['abc', 'ABD', 'aBe']
    print(L)  # ['abc', 'ABD', 'aBe']

    L.sort()
    print(L)  # ['ABD', 'aBe', 'abc']
    print('')

    L = ['abc', 'ABD', 'aBe']
    print(L)  # ['abc', 'ABD', 'aBe']

    # use the sort method's key, keyword argument to sort a list by some
    # comparison function
    L.sort(key=str.lower)  # normalize to lowercase
    print(L)  # ['abc','ABD','aBe']
    print('')

    L = ['abc', 'ABD', 'aBe']
    print(L)  # ['abc', 'ABD', 'aBe']

    # use the sort method's reverse keyword argument to sort an interable in
    # reverse order
    L.sort(key=str.lower, reverse=True)  # change sort order
    print(L)  # ['aBe','ABD','abc']
    print('')

    L = ['abc', 'ABD', 'aBe']
    print(L)  # ['abc', 'ABD', 'aBe']

    # the sorted() function returns a new list that is sorted
    # it does not modify the list it received
    L = sorted(L, key=str.lower, reverse=True)
    print(L)  # ['aBe','ABD','abc']
    print('')

    L = ['abc', 'ABD', 'aBe']
    print(L)  # ['abc', 'ABD', 'aBe']
    L = sorted([x.lower() for x in L], reverse=True)  # transform
    print(L)  # ['abe','abd','abc']
