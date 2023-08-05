# usage: python3 generating_both_offsets_and_items_enumerate.py

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
    try:
        while True:
            print(next(E))  # (0,'s'), (1,'p'), (2,'a'), (3,'m')
    except StopIteration:
        pass
    print('')

    print([c * (i + 1) for (i, c) in enumerate(S)])  # ['s','pp','aaa','mmmm']
