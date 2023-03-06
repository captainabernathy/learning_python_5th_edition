if __name__ == '__main__':
    print('code snippets from pages 124-125\n')
    T = (1, 2, 3, 4)
    print(T)  # (1,2,3,4)

    # tuple concatenation
    print(T + (5, 6))  # (1,2,3,4,5,6)

    # tuple indexing
    print(T[0])  # 1

    # get index an element appears at via index() method
    print(T.index(4))  # 3

    # get number of times an element appears with the count() method
    print(T.count(4))  # 1

    # tuples are immutable, so...
    # T[0] = 2  # is an error

    # use concatenation to create a new tuple
    T = (2,) + T[1:]
    print(T)  # (2,2,3,4)

    print(T.index(2))  # 0... first index where 2 is found
    print(T.count(2))  # 2

    # it's the comman that creates a tuple...
    T = 'spam', 3.0, [11, 22, 33]
    print(T)  # ('spam',3.0,[11,22,33])

    # index into the tuple's list...
    print(T[2][1])  # 22
