# usage: python3 function_introspection_and_attributes.py

def func(a):
    b = 'spam'
    return b * a


def f():
    pass


if __name__ == '__main__':
    print('code snippets from pages 586-587\n')

    print(func(8))  # spam 8 times
    print('')
    print(func.__name__)  # func... __name__ attribute
    print(dir(func))  # list of func's attributes
    print('')
    print(func.__code__)  # <code object func at 0x..., file "path", line #>
    print('')
    print(dir(func.__code__))  # attributes of func's __code__ object
    print('')
    print(func.__code__.co_varnames)  # ('a', 'b')... func's __code__ object's
                                      # variables
    print(func.__code__.co_argcount)  # 1... number of func's __code__ object's
                                      # arguments
    print('')

    print(func)  # <function func at 0x...>

    # attach user defined attributes to function
    func.count = 0
    func.count += 1
    print(func.count)  # 1
    print('')

    func.handles = 'Button-Press'
    print(func.handles)  # 'Button-Press'
    print(dir(func))  # count and handles now in func's attributes
    print('')

    print(dir(f))  # f's attributes
    print('')
    print(len(dir(f)))  # number of attributes belonging to f
    print('')

    # f's non-internal attributes
    print([x for x in dir(f) if not x.startswith('__')])
