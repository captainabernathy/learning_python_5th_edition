if __name__ == '__main__':
    print('code snippets from pages 410-411\n')
    # iterate over items in a list
    for x in ['spam', 'eggs', 'ham']:
        print(x, end=' ')  # spam eggs ham
    print('')

    s = 0
    for x in [1, 2, 3, 4]:
        s += x
    # NOTE: x persists after loop terminates
    print(x)  # 4
    print(s)  # 10
    print('')

    p = 1
    for item in [1, 2, 3, 4]:
        p *= item
    print(p)  # 24
    print('')

    S = 'lumberjack'
    T = ('and', 'I\'m', 'okay')
    # iterate over each letter in a string
    for x in S:
        print(x, end=' ')  # l u m b e r j a c k
    print('')

    # iterate over each item in a tuple
    for x in T:
        print(x, end=' ')  # and I'm okay
    print('')
