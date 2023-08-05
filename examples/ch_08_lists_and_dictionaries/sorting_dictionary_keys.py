# usage: python3 sorting_dictionary_keys.py

if __name__ == '__main__':
    print('code snippets from pages 278-280\n')

    D = {'a': 1, 'b': 2, 'c': 3}  # dictionary with 3 keys
    print(D)

    K = list(D.keys())  # ['a','b','c']
    print(K)
    print('')

    Ks = D.keys()  # iterable view object
    # sort iterable object and use iterator to index into dictionary
    for k in sorted(Ks):
        print('{}=>{}'.format(k, D[k]), end=' ')  # a=>1 b=>2 c=>3
    print('')

    # NOTE: dictionary iterators return keys
    for k in sorted(D):  # same as ^^^
        print('{}=>{}'.format(k, D[k]), end=' ')
    print('\n')

    # in tests for key membership in a dictionary
    print('c' in D)  # True
    print('x' in D)  # False
    print(D.get('c'))  # 3
    print(D.get('x'))  # None
    print('')

    if D.get('c') is not None:  # index on key if it's not None
        print('present', D['c'])
