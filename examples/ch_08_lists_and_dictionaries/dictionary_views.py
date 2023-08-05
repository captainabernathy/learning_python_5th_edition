# usage: python3 dictionary_views.py

if __name__ == '__main__':
    print('code snippets from pages 276-277\n')

    D = dict(a=1, b=2, c=3)  # build a dictionary
    print(D)
    print('')

    # NOTE: a dictionary's keys() method returns an iterable view object...
    # NOT a list
    K = D.keys()
    print(K)  # view object
    print('')
    print(list(K))  # ['a','b','c']
    print('')

    # NOTE: a dictionary's values() method returns an iterable view object...
    # NOT a list
    V = D.values()
    print(V)  # view object
    print('')
    print(list(V))  # [1,2,3]
    print('')

    # NOTE: a dictionary's items() method returns an iterable view object...
    # NOT a list
    print(D.items())  # view object
    print(list(D.items()))
    print('')

    for k in D.keys():
        print(k, end=' ')  # a b c
    print('\n')

    for key in D:  # same as ^^^
        print(key, end=' ')  # a b c
    print('')

    del D['b']  # change dictionary in place with del statement
    print(D)
    print(list(K))  # changes reflected  # ['a','c']
    print(list(V))  # changes reflected  # [1,3]
