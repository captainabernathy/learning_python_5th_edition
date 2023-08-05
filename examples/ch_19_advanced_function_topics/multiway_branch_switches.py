# usage: python3 multiway_branch_switches.py

# function returns 4... 2 + 2
def f1():
    return 2 + 2


# function returns 8... 2 * 8
def f2():
    return 2 * 4


# function returns 64... 2 ** 6
def f3():
    return 2 ** 6


if __name__ == '__main__':
    print('code snippets from pages 592-593\n')

    key = 'got'
    # a dictionary of lambda functions equivalent to f1(), f2(), f3()
    x = {'already': (lambda: 2 + 2),
         'got': (lambda: 2 * 4),
         'one': (lambda: 2 ** 6)}[key]()  # call to 2nd lambda function

    print(x)  # 8... 2 * 4
    print('')

    key = 'one'
    x = {'already': f1, 'got': f2, 'one': f3}[key]
    print(x())  # 64... 2 ** 6
