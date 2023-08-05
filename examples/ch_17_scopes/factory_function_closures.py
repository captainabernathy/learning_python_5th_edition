# usage: python3 factory_function_closures.py

# returns a handle to an enclosed function that subsequently raises the value
# passed to it by N
def maker(N):
    # NOTE: a nested function can retain access to the arguments passed to
    # the function that encloses it
    def action(X):
        return X ** N
    return action


# alternatively, return a lambda function that subsequently raises the value
# passed to it by N
def maker_lambda(N):
    # NOTE: lambda functions also retain state from the function that encloses
    # it
    return lambda X: X ** N


if __name__ == '__main__':
    print('code snippets from pages 522-523\n')

    # f is handle to a function that will return the square of the value of the
    # argument subsequnetly passed to it
    f = maker(2)
    print(f(3))  # 9... 3 ** 2
    print(f(4))  # 16... 4 ** 2
    print('')

    # g is handle to a function that will return the cube of the value of the
    # argument subsequnetly passed to it
    g = maker(3)
    print(g(4))  # 64... 4 ** 3
    print(f(4))  # 16... 4 ** 2
    print('')

    # h is a handle to a lambda function that will return the cube of the value
    # of the argument subsequently passed to it
    h = maker_lambda(3)
    print(h(4))  # 64... 4 ** 3
