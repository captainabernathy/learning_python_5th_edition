# usage: python3 decorator4.py

# state via enclosing scope and nonlocal instead of class attrs or global
def tracer(func):
    calls = 0

    def wrapper(*args, **kwargs):  # calls is per-function, NOT global
        nonlocal calls  # NOTE: 3X only
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper


@tracer
def spam(a, b, c):  # spam = tracer(spam)
    print(a + b + c)


@tracer
def eggs(x, y):  # eggs = tracer(eggs)
    print(x ** y)


# for illustrative purposes...
def spam1(a, b, c):
    print(a + b + c)


def eggs1(x, y):
    print(x ** y)


if __name__ == '__main__':
    print('code snippets from page 1332\n')

    spam(1, 2, 3)  # call 1 to spam... 6
    print('')

    spam(a=4, b=5, c=6)  # call 2 to spam... 15
    print('')

    eggs(2, 16)  # call 1 to eggs... 65536
    print('')

    eggs(4, y=4)  # call 2 to eggs... 256
    print('')

    ts = tracer(spam1)

    ts(1, 2, 3)  # call 1 to spam1... 6
    print('')

    ts(a=4, b=5, c=6)  # call 2 to spam1... 15
    print('')

    te = tracer(eggs1)

    te(2, 16)  # call 1 to eggs1... 65536
    print('')

    te(4, y=4)  # call 2 to eggs1... 256
    print('')
