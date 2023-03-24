# function that returns a list that consist of the square of the numbers of
# [0,n-1]
def buildsquares(n):
    res = []
    for i in range(n):
        res.append(i ** 2)
    return res


# function splits a comma-separated string and yields the result of
# capitalizing each part to the caller
def ups(line):
    for sub in line.split(','):
        yield sub.upper()


if __name__ == '__main__':
    print('code snippets from pages 617-618\n')
    for x in buildsquares(5):
        print(x, end=' : ')  # 0 1 4 9 16
    print('\n')

    # same as ^^^ with a list comprehension
    for x in [n ** 2 for n in range(5)]:
        print(x, end=' : ')  # 0 1 4 9 16
    print('\n')

    # same as ^^^ by mapping a lambda function
    for x in map(lambda n: n ** 2, range(5)):
        print(x, end=' : ')  # 0 1 4 9 16
    print('\n')

    print(tuple(ups('aaa,bbb,ccc')))  # ('AAA','BBB','CCC')
