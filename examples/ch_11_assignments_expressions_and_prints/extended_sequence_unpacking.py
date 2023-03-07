if __name__ == '__main__':
    print('code snippets from pages 355-358\n')
    seq = [1, 2, 3, 4]
    print(seq)  # [1,2,3,4]

    a, b, c, d = seq
    print(a, b, c, d)  # 1 2 3 4
    print('')

    # NOTE: the starred name is assigned to a list
    a, *b = seq  # assign first element in seq to a and the rest to b
    print(a, b)  # 1 [2,3,4]
    print('')

    # assign everything up to the last element in seq to a and the rest to b
    *a, b = seq
    print(a, b)  # [1,2,3] 4
    print('')

    # assign the first element in seq to a, everything up to the last element
    # in seq to b, and the last element in seq to c
    a, *b, c = seq  # first, rest, last
    print(a, b, c)  # 1 [2,3] 4
    print('')

    # assign the first element in seq to a, the second to b, and the rest to c
    a, b, *c = seq  # first, second, rest
    print(a, b, c)  # 1 2 [3,4]
    print('')

    # assign first letter of spam to a and the rest to b
    a, *b = 'spam'
    print(a, b)  # s pam
    print('')

    # assing the first letter of spam to a, everything up to the last letter to
    # b, and the last letter to c
    a, *b, c = 'spam'
    print(a, b, c)  # s pa m
    print('')

    # assign first element of range object to a, everything up to the last
    # element to b, and the last element to c
    a, *b, c = range(4)  # (0, [1, 2], 3)
    print(a, b, c)  # 0 [1,2] 3
    print('')

    # NOTE: slices are type-specific... "*assignment always returns a list"
    S = 'spam'
    print(S[0], S[1:])  # s pam
    print('')

    print(S[0], S[1:3], S[3])  # s pa m
    print('')

    L = [1, 2, 3, 4]
    while L:
        # assign first element in L to front, the overwrite L with the
        # remaining values
        front, *L = L  # get first, rest without slicing
        print(front, L)  # 1 [2,3,4], 2 [3,4], 3 [4], 4 []
    print('')

    seq = [1, 2, 3, 4]
    print(seq)  # [1,2,3,4]

    # assign first 3 elements in seq to a, b, and c and the rest to d
    a, b, c, *d = seq
    print(a, b, c, d)  # 1 2 3 [4]... d is a list

    # assign first 4 elements in seq to a, b, c, and d, and the rest to e
    a, b, c, d, *e = seq  # NOTE: here e gets an empty list
    print(a, b, c, d, e)  # 1 2 3 4 []

    # NOTE: regardless of where the starred name appears, if there is nothing
    # left to match it, it is always assinged the empty list
    a, b, *e, c, d = seq  # e still gets an empty list
    print(a, b, c, d, e)  # 1 2 3 4 []
    print('')

    # assign first element in seq to a and the rest to b
    a, *b = seq
    print(a, b)  # 1 [2,3,4]

    # same as ^^^
    a, b = seq[0], seq[1:]  # first, rest traditional
    print(a, b)  # 1 [2,3,4]
    print('')

    # assign everything up to the last element in seq to a and the last element
    # to b
    *a, b = seq  # rest, last
    print(a, b)  # [1,2,3] 4

    a, b = seq[:-1], seq[-1]  # rest, last traditional
    print(a, b)  # [1,2,3] 4
