# usage: python3 class_decorators.py

def decorator(cls):  # runs on @decorator
    class Wrapper:
        def __init__(self, *args):  # runs on instance creation
            self.wrapped = cls(*args)

        def __getattr__(self, name):  # runs on attribute lookup
            return getattr(self.wrapped, name)
    return Wrapper


@decorator
class C:  # C = decorator(C)
    def __init__(self, x, y):  # run by Wrapper __init__()
        self.attr = 'spam'


if __name__ == '__main__':
    print('code snippets from page 1323\n')

    x = C(6, 7)  # calls Wrapper(6, 7)
    print(x.attr)  # spam... runs Wrapper __getattr__()
    print(decorator(C)(6, 7).__getattr__('attr'))  # same as ^^^
    print('')
