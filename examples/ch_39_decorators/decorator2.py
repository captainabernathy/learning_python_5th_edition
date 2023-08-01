# this version of tracer differs from the one in decorator1.py in that it also
# forwards positional arguments
class tracer:  # state via instance attributes
    def __init__(self, func):  # runs on @tracer decorator
        self.calls = 0
        self.func = func  # save func for later call

    def __call__(self, *args, **kwargs):  # runs on calls to decorated function
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):  # spam = tracer(spam) => tracer.__init__(spam)
    print(a + b + c)


@tracer
def eggs(x, y):  # same as eggs = tracer(eggs)
    print(x ** y)  # wraps eggs in a tracer object


# for illustrative purposes...
def spam1(a, b, c):
    print(a + b + c)


def eggs1(x, y):
    print(x ** y)


if __name__ == '__main__':
    print('code snippets from page 1330\n')

    spam(1, 2, 3)  # call 1 to spam... 6
    print('')

    spam(a=4, b=5, c=6)  # call 2 to spam... 15
    print('')

    # calls tracer instance... where self.func = eggs
    # NOTE: self.calls is per-decoration here
    eggs(2, 16)  # call 1 to eggs... 65536
    print('')

    eggs(4, y=4)  # call 2 o eggs... 256
    print('')

    ts = tracer(spam1)
    ts(1, 2, 3)  # call 1 to spam1... 6
    print('')

    ts(a=4, b=5, c=6)  # call 2 to spam1 15
    print('')

    te = tracer(eggs1)

    te(2, 16)  # call 1 to eggs1... 65536
    print('')

    te(4, y=4)  # call 2 to eggs1... 256
    print('')
