if __name__ == '__main__':
    print('code snippets from pages 414-415\n')
    items = ['aaa', 111, (4, 5), 2.01]
    tests = [(4, 5), 3.14]

    # search for the elements in tests in the list items
    for key in tests:
        for item in items:
            if item == key:
                print(key, "was found")
                break
        else:
            print(key, "not found")
    print('')

    # similarly
    for key in tests:
        if key in items:
            print(key, "was found")
        else:
            print(key, "not found")
    print('')

    s1 = 'spam'
    s2 = 'scam'
    # make a list of elements of s1 that are in s2
    res = []  # start empty
    for x in s1:
        if x in s2:
            res.append(x)
    print(s1)  # spam
    print(s2)  # scam
    print(res)  # ['s','a','m']
    print('')

    # similarly a list comprehension...
    res = [x for x in s1 if x in s2]
    print(res)  # ['s','a','m']
