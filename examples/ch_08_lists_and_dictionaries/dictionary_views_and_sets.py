if __name__ == '__main__':
    print('code snippets from page 278\n')
    D = dict(a=1, b=None, c=3)  # dictionary with 3 keys
    K = D.keys()  # key view
    V = D.values()  # values view

    print(D)
    print(list(K))  # ['a','b','c']
    print(list(V))  # [1,None,3]
    print('')

    # keys (and some items) are set-like
    print(K | {'x': 4})  # set union {'a','b','c','x'}

    # intersect key views
    print(D.keys() & D.keys())  # {'a','b','c'}

    # intersect keys and set
    print(D.keys() & {'b'})  # {'b'}

    # intersect keys and dict
    print(D.keys() & {'b': 1})  # {'b'}

    # union keys and set
    print(D.keys() | {'b', 'c', 'd'})  # {'b','c'}
    print('')

    D = {'a': 1}
    print(D)
    # items views are set-like if they hashable
    print(list(D.items()))

    # union view and view
    print(D.items() | D.keys())  # {('a',1), 'a'}

    # dict treated same as its keys
    print(D.items() | D)  # {('a',1), 'a'}

    # union with set of key/value pairs
    print(D.items() | {('c', 3), ('d', 4)})  # {('a',1),('c',3),('d',4)}

    # the dictionary constructor  accepts iterable sets too
    print(dict(D.items() | {('c', 3), ('d', 4)}))
