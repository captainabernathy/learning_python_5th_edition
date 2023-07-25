# provides a handle to a nested function that maintains state through its
# enclosing scope
def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)

    oncall.calls = 0
    return oncall


def spam(a, b, c):
    return a + b + c


# calls to spam() now call tracer's nested function, which will call spam()
# as previously defined and forward any arguments provided in the call along
# with it
spam = tracer(spam)


class C:
    @tracer
    def spam(self, a, b, c):
        return a + b + c

    def spam2(self, a, b, c):
        return a + b + c

    # now calls to spam2() through instance of C are functionally equivalent
    # to calls to spam() though instances of C, since spam is decorated with
    # @tracer
    spam2 = tracer(spam2)


if __name__ == '__main__':
    print('code snippets from pages 1073-1074\n')

    x = C()
    print(x.spam(1, 2, 3))  # call 1 to spam, 6
    print(x.spam('a', 'b', 'c'))  # call 2 to spam, abc
    print('')

    print(C.spam(x, 1, 2, 3))  # call 3 to spam, 6
    print(C.spam(x, 'a', 'b', 'c'))  # call 4 to spam, abc
    print('')

    print(C.spam(C(), 1, 2, 3))  # call 5 to spam, 6
    print(C.spam(C(), 'a', 'b', 'c'))  # call 6 to spam, abc
    print('')

    print(x.spam2(1, 2, 3))  # call 1 to spam2, 6
    print(x.spam2('a', 'b', 'c'))  # call 2 to spam2, abc
    print('')

    print(C.spam2(x, 1, 2, 3))  # call 3 to spam2, 6
    print(C.spam2(x, 'a', 'b', 'c'))  # call 4 to spam2, abc
    print('')

    print(C.spam2(C(), 1, 2, 3))  # call 5 to spam2, 6
    print(C.spam2(C(), 'a', 'b', 'c'))  # call 6 to spam2, abc
    print('')

    print(spam(1, 2, 3))  # call 1 to spam, 6
    print(spam('a', 'b', 'c'))  # call 2 to spam, abc

