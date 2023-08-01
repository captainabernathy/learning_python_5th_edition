class tracer:
    # runs on @tracer decoration
    def __init__(self, func):
        self.calls = 0  # initialize calls
        self.func = func  # save original func(-tion)

    # runs on calls to decorated functions
    def __call__(self, *args):
        self.calls += 1  # increment calls
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)  # forward args in call to original function


@tracer
def spam(a, b, c):  # spam = tracer(spam)
    print(a + b + c)  # wraps spam in decorator object


# for illustrative purposes
calls = 0


def tracer1(func, *args):
    global calls
    calls += 1
    print('call %s to %s' % (calls, func.__name__))
    func(*args)


def spam1(a, b, c):
    print(a + b + c)


if __name__ == '__main__':
    print('code snippets from pages 1328-1329\n')

    spam(1, 2, 3)  # call 1 to spam... 6
    print('')

    spam('a', 'b', 'c')  # call 2 to spam... abc
    print('')

    print(spam.calls)  # 2
    print('')

    print(spam)  # <decorator1.tracer object at 0x...>
    print('')

    tracer1(spam1, 1, 2, 3)  # call 1 to spam1... 6
    print('')

    tracer1(spam1, 'a', 'b', 'c')  # call 2 to spam1... abc
    print('')

    print(calls)  # 2
