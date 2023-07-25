if __name__ == '__main__':
    print('code snippets from page 456-457\n')
    D = dict(a=1, b=2, c=3)
    print(D)
    print('')

    # NOTE: a dictionary object's keys() method returns an iterable dict_keys()
    # object
    K = D.keys()
    print(K)  # dict_keys(['a','b','c'])... a view object

    # NOTE: a view object is not its own iterator
    try:
        print(next(K))  # views are not iterators!!!
    except TypeError as ex:
        print(ex)  # 'dict_keys' object is not an iterator
    print('')

    It = iter(K)
    print(next(It))  # a
    print(D[next(It)])  # 2
    print('')

    for k in D.keys():  # all iteration contexts use auto
        print(k, D[k], end=' ')  # a 1 b 2 c 3
    print('\n')

    # use the list() constructor to convert a view object into a list
    print(list(K))  # force into a list
    print('')

    # NOTE: a dictionary object's values() method returns an iterable
    # dict_values() object
    V = D.values()
    print(V)  # dict_values([1,2,3])
    print(list(V))  # force into a list
    print(list(V)[0])  # force list and index
    print(list(D.items()))  # force everything into a list
    print('')

    # NOTE: a dictionary object's items() method returns an iterable
    # dict_items() object
    for (k, v) in D.items():
        print(k, v, end=' ')  # a 1 b 2 c 3
    print('\n')

    print(D)  # {'a':1,'b':2,'c':3}
    print('')

    # NOTE: dictionary objects are iterable themselves
    It = iter(D)
    try:
        while True:
            k = next(It)
            print(k, D[k], end=' ')  # a 1 b 2 c 3
    except StopIteration:
        pass
    print('\n')

    for key in D:  # no need to call D.keys() explicitly to iterate
        print(key, D[key], end=' ')  # a 1 b 2 c 3
    print('')
    print(D)  # {'a':1,'b':2,'c':3}
    print('')

    # NOTE: to iterate over a dictionary by sorted keys, it is necessary to
    # used the sorted() function to convert a keys object to a list
    for k in sorted(D.keys()):
        print(k, D[k], end=' ')  # a 1 b 2 c 3
    print('')
    print(D)  # {'a':1,'b':2,'c':3}
    print('')

    # NOTE: calling the sorted() function on a dictionary object implicitly
    # returns a list that is sorted by key
    for k in sorted(D):  # key sorting... best practice
        print(k, D[k], end=' ')  # a 1 b 2 c 3
    print('')
