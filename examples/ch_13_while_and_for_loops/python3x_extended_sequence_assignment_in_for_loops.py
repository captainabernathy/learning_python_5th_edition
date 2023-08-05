# usage: python3 python3x_extended_sequence_assignment_in_for_loops.py

if __name__ == '__main__':
    print('code snippets from page 413\n')

    a, b, c = (1, 2, 3)
    print(a, b, c)  # 1 2 3
    print('')

    for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
        print(a, b, c)  # 1 2 3, 4 5 6
    print('')

    # assign first element to a, last element to c, and everything else to b
    # NOTE: starred names are always assigned to lists
    a, *b, c = (1, 2, 3, 4)  # (1, [2, 3], 4)
    print(a, b, c)  # 1 [2,3] 4
    print('')

    # extended sequence assignment
    for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
        print(a, b, c)  # 1 [2,3] 4, 5 [6,7] 8
    print('')

    # manual slicing... for python2X
    for e in [(1, 2, 3, 4), (5, 6, 7, 8)]:
        a, b, c = e[0], e[1:3], e[3]
        print(a, b, c)  # 1 (2,3) 4, 5 (6,7)
