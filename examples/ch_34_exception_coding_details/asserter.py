def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2


if __name__ == '__main__':
    print('code snippets from page 1152\n')

    try:
        f(1)
    except AssertionError as ex:
        print(ex)  # x must be negative
