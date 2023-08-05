# usage: python3 sets.py

if __name__ == '__main__':
    print('code snippets from pages 169-176\n')

    x = set('abcde')
    y = set('bdxyz')
    print(x)  # {'b', 'd', 'c', 'a', 'e'}
    print(y)  # {'b', 'd', 'z', 'y', 'x'}

    # set difference... in x but not in y
    print(x - y)  # {'a', 'c', 'e'}
    # set union... in either x or y
    print(x | y)  # {'c', 'e', 'y', 'a', 'z', 'd', 'b', 'x'}
    # set intersection in both x and y
    print(x & y)  # {'b', 'd'}
    # set symmetric difference in x or in y but not in both
    print(x ^ y)  # {'a', 'c', 'e', 'x', 'y', 'z'}

    print(x > y)  # False... superset
    print(x < y)  # False... subset
    print('e' in x)  # True... membership
    print('e' in 'Camelot', 22 in [11, 22, 33])  # True, True... membership

    z = x.intersection(y)
    print(z)  # {'d', 'b'} same as x & y

    z.add('SPAM')  # insert one item
    print(z)  # {'SPAM', 'd', 'b'}

    z.update(set(['X', 'Y']))  # in-place merge
    print(z)  # {'SPAM', 'd', 'b', 'X', 'Y'}

    z.remove('b')  # delete one item
    print(z)  # {'SPAM', 'd', 'X', 'Y'}

    # iteration
    for item in set('abc'):
        print(item * 3)  # print each item 3 times

    S = set([1, 2, 3])
    print(S)  # {1, 2, 3}
    # print(S | [3, 4])  # error: set and list, instead...
    print(S.union([3, 4]))  # {1, 2, 3, 4}

    print(S.intersection((1, 3, 5)))  # {1, 3}
    print(S.issubset(range(-5, 5)))  # True
    print('')

    # set literals
    print(set([1, 2, 3, 4]))  # {1,2,3,4} built-in call
    print({1, 2, 3, 4})  # {1,2,3,4} 2.7, 3.X
    print(set('spam'))  # {'s', 'p', 'a', 'm'} add all items in an iterable

    S = {'s', 'p', 'a', 'm'}
    print(S)  # {'s', 'p', 'a', 'm'}
    S.add('alot')  # 'alot' is a single item
    print(S)  # {'s', 'p', 'a', 'm', 'alot'}

    S1 = {1, 2, 3, 4}
    print(S1)  # {1,2,3,4}
    print(S1 & {1, 3})  # {1,3} set intersection
    print({1, 5, 3, 6} | S1)  # {1,2,3,4,5,6} set union
    print(S1 - {1, 3, 4})  # {2} set difference
    print(S1 > {1, 3})  # superset: True
    print(S1 - {1, 2, 3, 4})  # empty set: set()
    print(type({}))  # <class, dict>... bc {} is a dictionary

    # initialize empty set
    S = set()
    S.add(1.23)
    print(S)  # {1.23}

    print({1, 2, 3} | {3, 4})  # {1,2,3,4} union
    print({1, 2, 3}.union([3, 4]))  # {1,2,3,4} same
    print({1, 2, 3}.union({3, 4}))  # {1,2,3,4} same
    print({1, 2, 3}.union(set([3, 4])))  # {1,2,3,4} same
    print({1, 2, 3}.intersection((1, 3, 5)))  # {1, 3}
    print({1, 2, 3}.issubset(range(-5, 5)))  # True
    print('')

    # immutable constraints and frozen sets
    # S.add([1, 2, 3])  # only immutable objects work in a set
    # S.add({'a':1})  # only immutable objects work in a set
    S.add((1, 2, 3))  # ok since tuples are immutable
    print(S)  # {1.23, (1, 2, 3)}
    print(S | {(4, 5, 6), (1, 2, 3)})  # {1.23, (1,2,3), (4,5,6)}
    print((1, 2, 3) in S)  # True
    print((1, 4, 3) in S)  # False
    print('')

    # set comprehensions
    print({x ** 2 for x in [1, 2, 3, 4]})  # {1,4,9,16}
    print({x for x in 'spam'})  # {'s', 'p', 'a', 'm'}
    print({c * 4 for c in 'spam'})

    S = {c * 4 for c in 'spam'}
    print(S)
    print(S | {'mmmm', 'xxxx'})  # union
    print(S & {'mmmm', 'xxxx'})  # intersection
    print('')

    L = [1, 2, 1, 3, 2, 4, 5]
    print(L)  # [1,2,1,3,2,4,5]
    print(set(L))  # {1, 2, 3, 4, 5}

    # remove duplicates
    L = list(set(L))
    print(L)  # [1,2,3,4,5]

    print(list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa'])))
    print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))  # difference {3, 7}
    print(set('abcdefg') - set('abdghi'))  # {'c', 'e', 'f'}
    print(set('spam') - set(['h', 'a', 'm']))  # mixed types {'p', 's'}

    # in bytes but not bytearray
    print(set(dir(bytes)) - set(dir(bytearray)))
    # in bytearray but not bytes
    print(set(dir(bytearray)) - set(dir(bytes)))

    # order matters in sequences
    L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
    print(L1)
    print(L2)
    print(L1 == L2)  # False
    print(set(L1) == set(L2))  # True
    print(sorted(L1) == sorted(L2))  # True

    # False, True, True
    print('spam' == 'asmp', set('spam') == set('asmp'),
          sorted('spam') == sorted('asmp'))

    engineers = {'bob', 'sue', 'ann', 'vic'}
    managers = {'tom', 'sue'}
    print('bob' in engineers)  # True
    print(engineers & managers)  # {'sue'} intersection
    print(engineers | managers)  # {'bob', 'sue', 'ann', 'vic', 'tom'} union
    print(engineers - managers)  # {'bob', 'ann', 'vic'} difference
    # symmetric difference
    print(engineers ^ managers)  # {'bob', 'ann', 'vic', 'tom'}
    print(engineers > managers)  # False superset: are all engineers managers?
    # subset: are bob and sue engineers?
    print({'bob', 'sue'} < engineers)  # True
    print((managers | engineers) > engineers)  # True... > -> superset operator

    # set intersection... the hard way
    print((managers | engineers) - (managers ^ engineers))  # {'sue'}
