# skeleton for using decorator arguments to perform range testing in 3X and 2X
def rangetest_deco(**argchecks):
    def on_decorator(func):
        def on_call(*pargs, **kargs):
            print(argchecks)
            for check in argchecks:
                pass  # add validation code here
            return func(*pargs, **kargs)  # return results of call
        return on_call  # return on_call handle
    return on_decorator  # return on_decorator handle


# NOTE: function annotations are available in 3X only
# skeleton for using function annotations to perform range checking
def rangetest_anno(func):
    def on_call(*pargs, **kargs):
        argchecks = func.__annotations__
        print(argchecks)
        for check in argchecks:
            pass  # add validation code here
        return func(*pargs, **kargs)  # return results of call
    return on_call  # return on_call handle


@rangetest_deco(a=(1, 5), c=(0.0, 1.0))
def f1(a, b, c):
    print(a + b + c)


@rangetest_anno
def f2(a: (1, 5), b, c: (0.0, 1.0)):
    print(a + b + c)


if __name__ == '__main__':
    print('code snippets from pages 1387-1388\n')

    f1(1, 2, c=3)  # {'a':(1,5), 'c':(0.0,1.0)}... 6
    print('')

    f2(1, 2, c=3)  # {'a': (1,5), 'c':(0.0, 1.0)}... 6
    print('')
