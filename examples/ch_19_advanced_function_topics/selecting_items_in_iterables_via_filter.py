if __name__ == '__main__':
    print('code snippets from page 599\n')
    print(list(range(-5, 5)))  # [-5,-4,-3,-2,-1,0,1,2,3,4]
    print('')

    # NOTE: filter() evaluates an expression against a sequence and returns
    # the results for which the expression evaluated to True
    print(list(filter((lambda x: x > 0), range(-5, 5))))  # [1,2,3,4]
    print('')

    res = []  # same as ^^^
    for x in range(-5, 5):
        if x > 0:
            res.append(x)

    print(res)  # [1,2,3,4]
    print('')

    # emulating filter() with a list comprehension
    print([x for x in range(-5, 5) if x > 0])  # [1,2,3,4]
