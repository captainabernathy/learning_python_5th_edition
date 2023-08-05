# usage: python3 sequence_assignments.py

if __name__ == '__main__':
    print('code snippets from pages 351-352\n')

    nudge = 1
    wink = 2
    print(nudge, wink)  # 1 2
    print('')

    r1 = A, B = nudge, wink  # tuple assignment
    print(r1)  # (1,2)
    print(A, B)  # 1 2
    print('')

    r2 = [C, D] = [nudge, wink]  # list assignment
    print(r2)  # [1,2]
    print(C, D)  # 1 2
    print('')

    wink, nudge = nudge, wink  # swap variable values
    print(nudge, wink)  # 2 1
    print('')

    r3 = [a, b, c] = (1, 2, 3)  # assign tuple of values to list of names
    r4 = [a, b, c]
    # NOTE: r3 is a tuple, but r4 is a list
    print(r3)  # (1,2,3)
    print(r4)
    print(a, b, c)  # 1 2 3
    print('')

    r5 = (a, b, c) = "ABC"  # assign string of characters to tuple of names
    r6 = (a, b, c)
    # NOTE: r5 is a string, but r6 is a tuple
    print(r5)  # ABC
    print(r6)  # ('A','B','C')
    print(a, b, c)  # A B C
