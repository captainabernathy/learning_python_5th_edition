# usage: python3 multiple_target_assignments.py

if __name__ == '__main__':
    print('code snippets from pages 359-360\n')

    a = b = c = 'spam'
    print(a, b, c)  # spam spam spam

    # same as ^^^
    c = 'spam'
    b = c
    a = b
    print(a, b, c)
    print('')

    a = b = 0
    b = b + 1
    print(a, b)  # 0 1
    print('')

    a = b = []  # a and b share the same reference to the empty list
    print(a, b)  # [] []
    b.append(42)  # this also appends 42 to a
    print(a, b)  # [42] [42]

    a = []  # a is an empty list
    b = []  # b is an empty list
    print(a, b)  # [] []
    # NOTE: since a and b do not share a reference, changes to one does not
    # affect the other
    b.append(42)  # a is still empty
    print(a, b)  # [] [42]

    a, b = [], []  # same as ^^
    print(a, b)  # [] []
    b.append(42)  # a is still empty
    print(a, b)  # [] [42]
