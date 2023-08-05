# usage: python3 tracer1.py

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)


# the decoration @tracer is equivalent to...
# spam = tracer(spam)
# calling spam() now invokes __call__() for tracer instances forwarding any
# arguments passed to spam() along the way
@tracer
def spam(a, b, c):
    return a + b + c


def spam2(a, b, c):
    return a + b + c


# now calls to spam2() are bound to tracer's __call__() method for instances
spam2 = tracer(spam2)


def spam3(a, b, c):
    return a + b + c


if __name__ == '__main__':
    print('code snippets from pages 1072-1073\n')

    print(spam(1, 2, 3))  # call 1 to spam, 6
    print(spam('a', 'b', 'c'))  # call 2 to spam, abc
    print('')

    print(spam2(1, 2, 3))  # call 1 to spam2, 6
    print(spam2('a', 'b', 'c'))  # call 2 to spam2, abc
    print('')

    # t is an instance of tracer, which provides a __call__() operator for
    # instances... which is now invoked for calls to t()
    t = tracer(spam3)
    print(t(1, 2, 3))  # call 1 to spam3, 6
    print(t('a', 'b', 'c'))  # call 2 to spam3, abc
    print('')

    print(tracer.__call__(t, 1, 2, 3))  # call 3 to spam3, 6
    print(tracer.__call__(t, 'a', 'b', 'c'))  # call 4 to spam3, abc
    
