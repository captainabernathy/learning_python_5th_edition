if __name__ == '__main__':
    print('code snippets from pages 129-130\n')
    # make a set with the set() constructor
    X = set('spam')
    print(X)  # {'a', 'm', 'p', 's'}... order not important

    # make a set with literals
    Y = {'h', 'a', 'm'}
    print(Y)  # {'a', 'h', 'm'}

    print(X, Y)

    # use & operator for set intersection
    print(X & Y)  # {'a', 'm'}

    # use | operator for set union
    print(X | Y)  # {'a', 'h', 'p', 's', 'm'}

    # use - operator for set difference
    print(X - Y)  # {'p', 's'}

    # use > to check if one set is a superset of another
    print(X > Y)  # False

    # set comprehension
    print({n ** 2 for n in [1, 2, 3, 4]})  # {16, 1, 4, 9}

    # duplicates are not included in the set
    print(set([1, 2, 1, 3, 1]))  # {1,2,3}

    # find difference b/t collections
    print(set('spam') - set('ham'))  # {'p', 's'}

    # sets have order-neutral equality
    print(set('spam') == set('asmp'))  # True

    # use in operator to test set membership
    print('p' in set('spam'))  # True
    print('p' in 'spam')  # True
    print('ham' in ['eggs', 'spam', 'ham'])  # True
