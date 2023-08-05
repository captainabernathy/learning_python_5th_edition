# usage: python3 other_built_in_type_iterables.py

import os

if __name__ == '__main__':
    print('code snippets from pages 438-440\n')

    D = {'a': 1, 'b': 2, 'c': 3}

    # NOTE: a dictionary object's keys() method returns an interable
    for key in D.keys():
        print(key, D[key])
    print('')

    # NOTE: in modern python, dictionaries are iterable themselves
    for key in D:
        print(key, D[key])
    print('')

    # NOTE: os.popen() can be used to read the output of shell commands
    P = os.popen('dir')

    print(P.__next__())

    # NOTE: popen() objects have an obj.__next()__ method but do NOT have an
    # obj.next() method and do NOT support the built-in next() function
    try:
        print(P.next())
    except AttributeError as ex:
        print(ex)
    print('')

    try:
        print(next(P))
    except TypeError as ex:
        print(ex)
    print('')

    # NOTE: in order to use the next() function with a popen object it is first
    # necessary construt an iterator for it with iter()
    It = iter(P)  # need to construct an iterator for a popen object
    print(next(It))
    print(It.__next__())

    # NOTE: even when constructed with an iterator, this object does not have
    # an obj.next() method
    try:
        It.next()
    except AttributeError as ex:
        print(ex)
    print('')

    R = range(5)  # <range object...>
    print(R)  # range(0,5)
    It = iter(R)
    print(next(It))  # 0
    print(next(It))  # 1
    print(It.__next__())  # 2

    # NOTE: range object iterators do NOT have a next() method
    try:
        It.next()
    except AttributeError as ex:
        print(ex)
    print('')

    # use the list() constructor to convert a range object to a list
    print(list(range(5)))  # [0,1,2,3,4]
    print('')

    # NOTE: an enumerate() object is an iterable object that contains
    # two-element tuples for each element in object it was constructed from.
    # the first element in this tuple is a number that corresponds to the
    # second element relative to that element's position in the underlying
    # object.
    s = 'spam'
    E = enumerate(s)  # enumerate is an iterable
    print(E)  # <enumerate object...>
    print('')

    It = iter(E)
    # generate results with iteration protocol
    print(next(It))  # (0,'s')
    t = next(It)
    print(t[0], t[1])  # 1 p
    print(s[next(It)[0]])  # a
    print(next(It)[1])  # m
    print('')

    # use the list() constructor to convert an enumerate object to list of
    # tuples
    L = list(enumerate(s))
    print(L)

    # use the dict() construct to convert a list of tuples to a dictionary
    print(dict(L))
