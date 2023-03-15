if __name__ == '__main__':
    print('code snippets from pages 422-425\n')
    L1 = [1, 2, 3, 4]
    L2 = [5, 6, 7, 8]
    print(L1)  # [1,2,3,4]
    print(L2)  # [5,6,7,8]

    # use the zip() funcion to create an object of pairwise tuples
    # use the list() constructor on a zip object to build a list of pairwise
    # tuples
    L3 = list(zip(L1, L2))  # create a list of tuples
    print(L3)  # [(1,5),(2,6),(3,7),(4,8)]
    print('')

    # iterate over each tuple in a zip object
    for (x, y) in zip(L1, L2):
        print(x, y, '--', x + y)  # 1 5 -- 6, 2 6 -- 8, 3 7 -- 10, 4 8 -- 12
    print('')

    T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
    print(T1)  # (1,2,3)
    print(T2)  # (4,5,6)
    print(T3)  # (7,8,9)

    T4 = list(zip(T1, T2, T3))
    print(T4)  # [(1,4,7),(2,5,8),(7,8,9)]
    print('')

    S1 = 'abc'
    S2 = 'xyz123'
    # NOTE: when zipped items differ in size, the zip object is truncated to
    # the lenght of the shortest element
    print(list(zip(S1, S2)))  # [('a','x'),('b','y'),('c','z')]

    M1 = map(None, S1, S2)  # map equivalent of ^^^ for 2X
    print(M1)  # map object in 3x
    print('')

    # list contains elements are the numeric values of the letters in spam
    R1 = list(map(ord, 'spam'))
    print(R1)  # [115,112,97,109]

    # ^^^ with a loop
    R2 = []
    for c in 'spam':
        R2.append(ord(c))
    print(R2)  # [115,112,97,109]
    print('')

    D1 = {'spam': 1, 'eggs': 3, 'toast': 5}
    print(D1)

    # ^^^ individually...
    D1 = {}  # empty dictionary
    D1['spam'] = 1
    D1['eggs'] = 2
    D1['toast'] = 5
    print(D1)
    print('')

    keys = ['spam', 'eggs', 'toast']
    vals = [1, 3, 5]
    L1 = list(zip(keys, vals))
    print(keys)
    print(vals)
    print(L1)  # [('spam',1),('eggs',3),('toast',5)]
    print('')

    # build up a dictionary by iterating over each tuple in a zip object
    # derived from a list of keys and values
    D2 = {}
    for (k, v) in zip(keys, vals):  # use zip with loop to build dict
        D2[k] = v
    print(D2)
    print('')

    # do ^^^ with a dictionary comprehension
    D3 = {k: v for (k, v) in zip(keys, vals)}
    print(D3)
    print('')

    # do ^^^ all at once with dict() constructor
    # use the dict() constructor to build a dictionary directly from a zip
    # object created from a list of keys and values
    D4 = dict(zip(keys, vals))
    print(D4)

