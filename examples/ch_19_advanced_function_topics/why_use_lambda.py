# function returns the square of its argument
def f1(x):
    return x ** 2


# function returns the cube of its argument
def f2(x):
    return x ** 3


# function returns the result of raising its argument to the power of four
def f3(x):
    return x ** 4


if __name__ == '__main__':
    print('code snippets from page 592\n')
    L = [lambda x: x ** 2,  # same as f1()
         lambda x: x ** 3,  # same as f2()
         lambda x: x ** 4]  # same as f3()

    for f in L:
        print(f(2))  # 4 8 16
    print('')

    print(L[0](3))  # 9... 3 ** 2
    print('')

    L = [f1, f2, f3]
    for f in L:
        print(f(2))  # 4 8 16
    print('')

    print(L[0](3))  # 9... 3 ** 2
