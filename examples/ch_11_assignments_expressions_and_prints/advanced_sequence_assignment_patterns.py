if __name__ == '__main__':
    print('code snippets from pages 353-354\n')
    string = 'SPAM'
    print(string)  # SPAM

    a, b, c, d = string  # same number on both sides
    print(a, b, c, d)  # S P A M

    a, b, c = string[0], string[1], string[2:]  # index and slice
    print(a, b, c)  # S P AM

    a, b, c = list(string[:2]) + [string[2:]]  # slice and concatenate
    print(a, b, c)  # S P AM

    # same as ^^^
    a, b = string[:2]
    c = string[2:]
    print(a, b, c)  # S P AM

    (a, b), c = string[:2], string[2:]  # nested sequences
    print(a, b, c)  # S P AM
    print('')

    red, green, blue = range(3)
    print(red, green, blue)  # 0 1 2
    print(list(range(3)))  # [0,1,2]
    print('')

    L = [1, 2, 3, 4]
    while L:
        front, L = L[0], L[1:]
        print(front, L)  # 1 [2,3,4], 2 [3,4], 3 [4], 4 []
