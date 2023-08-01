def d1(F):
    return F


def d2(F):
    return F


def d3(F):
    return F


def d11(F):
    return lambda: 'X' + F()


def d22(F):
    return lambda: 'Y' + F()


def d33(F):
    return lambda: 'Z' + F()


@d1
@d2
@d3
def func():  # func = d1(d2(d3(func)))
    print('spam')


@d11
@d22
@d33
def func1():  # func1 = d11(d22(d33(func1)))
    return 'spam'


def func2():
    return 'spam'


if __name__ == '__main__':
    print('code snippets from pages 1324-1326\n')

    func()  # spam
    print(d1(d2(d3(func2)))())  # spam... same as ^^^
    print('')

    print(func1())  # XYZspam
    print(d11(d22(d33(func2)))())  # XYZspam... same as ^^^
    print('')
