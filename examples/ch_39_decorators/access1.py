trace_me = False


def trace(*args):
    if trace_me:
        print('[' + ' '.join(map(str, args)) + ']')


# NOTE: the decorator catches and validates both attribute fetches and
# assignments run outside of the wrapped class but does not catch attribute
# accesses inside the class itself

# arguments are passed to the private() function, which returns the decorator
# function to be applied on the subject class... private() returns the
# decorator, which in turn 'remembers' the privates list as an enclosing scope
# reference
def private(*privates):
    # privates in enclosing scope
    # NOTE: the arguments to private() are used before decoration occurs and
    # are retained as an enclosing scope reference for use in both
    # on_decorator() and on_instance()
    def on_decorator(acls):
        # acls in enclosing scope wrapped in instance attribute
        # NOTE: the class argument to on_decorator() is used at decoration time
        # and is retained as an enclosing scope reference for use at instance
        # construction time
        class on_instance:
            # NOTE: the wrapped instance object is retained as an instance
            # attribute in the on_instance() proxy object for use when
            # attributes are later accessed from outside the class
            def __init__(self, *args, **kwargs):
                self.wrapped = acls(*args, **kwargs)

            # attribute accesses from outside the subject class are intercepted
            # by the wrapper layer's overloading methods and delegated to the
            # class if valid
            def __getattr__(self, attr):  # my attrs don't call getattr
                trace('get:', attr)  # others assumed in wrapped
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):  # outside accesses
                trace('set:', attr, value)  # others run normally
                if attr == 'wrapped':  # allow my attrs
                    self.__dict__[attr] = value  # avoid looping
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)  # wrapped obj attrs
        return on_instance
    return on_decorator


@private('data', 'size')
class Doubler:
    # Doubler = private('data','size')(Doubler)
    def __init__(self, label, start):
        self.label = label  # access inside the subject class
        self.data = start  # not intercepted: run normally

    # methods run with no checking bc privacy not inherited
    def size(self):
        return len(self.data)

    def double(self):
        for i in range(self.size()):
            self.data[i] = self.data[i] * 2

    def display(self):
        print('%s => %s' % (self.label, self.data))


# for illustrative purposes
class Doubler1:
    def __init__(self, label, start):
        self.label = label  # access inside the subject class
        self.data = start  # not intercepted: run normally

    # methods run with no checking bc privacy not inherited
    def size(self):
        return len(self.data)

    def double(self):
        for i in range(self.size()):
            self.data[i] = self.data[i] * 2

    def display(self):
        print('%s => %s' % (self.label, self.data))


if __name__ == '__main__':
    print('code snippets from pages 1361-1363\n')

    trace_me = True

    # [set: wrapped <__main__.Doubler object at 0x...>]
    X = Doubler('X is', [1, 2, 3])
    print('')

    # [set: wrapped <__main__.Doubler object at 0x...>]
    Y = Doubler('Y is', [-10, -20, -30])
    print('')

    print(X.label)  # [get: label]... X is
    print('')

    X.display()  # [get: display]... X is => [1,2,3]
    print('')

    X.double()  # [get: double]
    print('')

    X.display()  # [get: display]... X is => [2,4,6]
    print('\n')

    print(Y.label)  # [get: label]... Y is
    print('')

    Y.display()  # [get: display]... Y is [-10,-20,-30]
    print('')

    Y.double()  # [get: double]
    print('')

    Y.label = 'Spam'  # [set: label Spam]
    print('')

    Y.display()  # [get: display]... Spam => [-20,-40,-60]
    print('')

    try:
        print(X.size())  # [get: size]
    except TypeError as ex:
        print(ex)  # private attribute fetch: size
    print('')

    try:
        print(X.data)  # [get: data]
    except TypeError as ex:
        print(ex)  # private attribute fetch data
    print('')

    try:
        X.size = lambda S: 0  # [set: size <function <lambda> at 0x...]
    except TypeError as ex:
        print(ex)  # private attribute change: size
    print('')

    try:
        print(Y.data)  # [get: data]
    except TypeError as ex:
        print(ex)  # private attribute fetch: data
    print('')

    try:
        print(Y.size())  # [get: size]
    except TypeError as ex:
        print(ex)  # private attribute fetch: size
    print('')

    print('-' * 80)
    print('')

    # for illustrative purposes...

    # [set: wrapped <__main__.Doubler1 object at 0x...>]
    X1 = private('data', 'size')(Doubler1)('X1 is', [1, 2, 3])
    print('')

    print(X1.label)  # [get: label]... X1 is
    print('')

    X1.display()  # [get: display]... X1 is => [1,2,3]
    print('')

    X1.double()  # [get: double]
    print('')

    X1.label = 'Spam'  # [set: label Spam]
    print('')

    X1.display()  # Spam => [2,4,6]
    print('')
    
    try:
        print(X1.size())  # [get: size]
    except TypeError as ex:
        print(ex)  # private attribute fetch: size
    print('')

    try:
        print(X1.data)  # [get: data]
    except TypeError as ex:
        print(ex)  # private attribute fetch data
    print('')
