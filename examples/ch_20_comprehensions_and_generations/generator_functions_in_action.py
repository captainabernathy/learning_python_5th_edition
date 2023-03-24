# NOTE: a generator function yields its result to its caller... a yield
# statement suspends a function and sends a value back to the caller, but
# retains enough state to enable the function to resume from where it left
# off

# generator function that yields N results each of which corresponds to one of
# the squares of the numbers in the range [0,N-1]
def gensquares(N):
    for i in range(N):
        yield i ** 2


if __name__ == '__main__':
    print('code snippets from pages 615-617\n')
    for i in gensquares(5):
        print(i, end=' : ')  # 0 1 4 9 16
    print('\n')

    x = gensquares(4)
    print(x)  # <generator object...>

    # NOTE: the next() built-in function calls an object's __next__() method,
    # the __next__() method raises a StopIteration exception when the
    # generator is exhausted
    print(next(x))  # 0
    print(next(x))  # 1
    print(next(x))  # 4
    print(next(x))  # 9
    print('')

    y = gensquares(5)
    # NOTE: the top-level iter() call of the iteration protocol isn't required
    # for generator functions bc generators are their own iterator
    print(iter(y) is y)  # True
    print(next(y))  # 0
    print(next(y))  # 1
    print(next(y))  # 4
    print(next(y))  # 9
    print(next(y))  # 16
    print('')

