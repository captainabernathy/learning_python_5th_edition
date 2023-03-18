# function returns the result of calling the function passed to func with the
# positional arguments contained in pargs and the keyword arguments contained
# in kargs
def tracer(func, *pargs, **kargs):  # accept arbitrary arguments
    print('calling:', func.__name__)
    return func(*pargs, **kargs)  # pass along arbitrary arguments


def func(a, b, c, d):
    return a + b + c + d


if __name__ == '__main__':
    print('code snippets from page 558\n')
    print(tracer(func, 1, 2, c=3, d=4))  # 10
