if __name__ == '__main__':
    print('code snippets from page 438\n')
    L = [1, 2, 3]

    for X in L:  # automatic iteration
        print(X ** 2, end=' ')
    print('')

    It = iter(L)
    # book code... executes try block for each iteration and breaks on the
    # exception... inefficient
    while True:  # manual iteration
        try:
            X = next(It)
        except StopIteration:
            break
        print(X ** 2, end=' ')
    print('')

    It = iter(L)
    # instead of breaking on the exception... let the exception break the loop
    try:
        while True:
            print(next(It) ** 2, end=' ')
    except StopIteration:
        pass
    print('')
