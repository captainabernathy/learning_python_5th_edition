calls = 0


# state via enclosing scope and global instead of class attributed
def tracer(func):
    def wrapper(*args, **kwargs):
        global calls  # calls is global, not per-function
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
    print('code snippets from pages 1331-1332\n')
    
    spam(1, 2, 3)  # call 1 to spam... 6
    print('')

    spam(a=4, b=5, c=6)  # call 2 to spam... 15
    print('')

    eggs(2, 16)  # call 3 to eggs... 65536
    print('')

    eggs(4, y=4)  # call 4 to eggs... 256
    print('')

    ts = tracer(spam1)

    ts(1, 2, 3)  # call 5 to spam1... 6
    print('')

    ts(a=4, b=5, c=6)  # call 6 to spam1 15
    print('')

    te = tracer(eggs1)

    te(2, 16)  # call 7 to eggs1... 65536
    print('')

    te(4, y=4)  # call 8 to eggs1 256
    print('')
