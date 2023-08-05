# usage: python3 tuple_conversion_methods_and_immutability.py

if __name__ == '__main__':
    print('code snippets from pages 287-288\n')
    
    T = ('cc', 'aa', 'dd', 'bb')

    # convert tuple to list
    tmp = list(T)  # make list from tuple's items

    print(T)  # ('cc', 'aa', 'dd', 'bb')
    print(tmp)  # ['cc', 'aa', 'dd', 'bb']
    print('')

    tmp.sort()  # sort list

    # convert list to tuple
    TS = tuple(tmp)  # make tuple from list's items
    
    # NOTE: tuple's cannot be modified
    # or use built in sorted() method... remember, the sorted() method does NOT
    # sort in place and returns a list
    T = sorted(T)

    print(tmp)  # ['aa','bb','cc','dd']
    print(TS)  # ('aa','bb','cc','dd')
    print(T)  # ['aa','bb','cc','dd']
    print('')

    T = (1, 2, 3, 4, 5)
    # convert tuple to list with list comprehension
    L = [x + 20 for x in T]  # list from tuple
    print(T)  # (1,2,3,4,5)
    print(L)  # [21,22,23,24,25]
    print('')

    T = (1, 2, 3, 2, 4, 2)
    print(T)  # (1, 2, 3, 2, 4, 2)
    
    # tuples provide index() and count() methods
    print(T.index(2))  # 1... offset of first appearance of 2 in T
    print(T.index(2, 2))  # 3... offset of second 2 in T
    print(T.count(2))  # 3... number of 2s in T
    print('')

    T = (1, [2, 3], 4)
    print(T)  # (1, [2, 3], 4)

    # NOTE: a modifiable element contained in a tuple can be updated
    T[1][0] = 'spam'  # ok to change nested list in tuple
    print(T)  # (1, ['spam', 3], 4)
