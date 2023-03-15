if __name__ == '__main__':
    print('code snippets from pages 425-426\n')
    S = 'spam'
    offset = 0
    print(S)
    print(offset)
    print('')

    for item in S:
        print(item, 'appears at offset', offset)
        offset += 1
    print('')

    # doing ^^^ with enumerate()
    # NOTE: enumerate() returns a generator object that can be iterated over
    for (offset, item) in enumerate(S):
        print(item, 'appears at offset', offset)
    print('')

    E = enumerate(S)
    print(next(E))  # (0, 's')
    print(next(E))  # (1, 'p')
    print(next(E))  # (2, 'a')
    print(next(E))  # (3, 'm')
    # print(next(E))  # beyond bounds of object... StopIteration ERROR
    print('')

    # instead...
    E = enumerate(S)
    while True:
        try:
            print(next(E))
        except StopIteration:
            break
    print('')

    print([c * i for (i, c) in enumerate(S)])  # ['', 'p', 'aa', 'mmm']
