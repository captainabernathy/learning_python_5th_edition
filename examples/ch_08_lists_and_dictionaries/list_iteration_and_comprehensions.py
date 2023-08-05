# usage: python3 list_iteration_and_comprehensions.py

if __name__ == '__main__':
    print('code snippets from pages 250-251\n')

    # membership test
    print(3 in [1, 2, 3])  # True
    print('')

    # iteration
    for x in [1, 2, 3]:
        print(x, end=' ')  # 1 2 3
    print('\n')

    # list comprehension... returns a list
    res = [c * 4 for c in 'SPAM']
    print(res)  # ['SSSS','PPPP','AAAA','MMMM']
    print('')

    # same as
    res = []  # initialize an empty list
    for c in 'SPAM':
        res.append(c * 4)  # eppend elements to list

    print(res)  # ['SSSS','PPPP','AAAA','MMMM']
    print('')

    # map a function across a sequence
    print(list(map(abs, [-1, -2, 0, 1, 2])))  # [1, 2, 0, 1, 2]

    # same as
    res = map(abs, [-1, 2, 0, 1, 2])  # map function to a list

    # iterate over map object
    for i in res:
        print(i, end=' ')  # 1, 2, 0, 1, 2
    print('')

