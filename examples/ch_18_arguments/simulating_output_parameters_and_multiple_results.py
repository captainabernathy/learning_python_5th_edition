# usage: python3 simulating_output_parameters_and_multiple_results.py

# function returns a x and y as a tuple
def multiple(x, y):
    x = 2  # update local copy of a
    y = [3, 4]  # assign a new list to y
    return x, y  # return results as a tuple


if __name__ == '__main__':
    print('code snippets from page 548\n')

    X = 1
    L = [1, 2]
    D = {'a': 1}
    T = (1)
    print(X)  # 2
    print(L)  # [3,4]
    print(D)  # {'a':1}
    print(T)  # 1
    print('')

    X, L = multiple(X, L)  # assignment overwrites previous values of X and L
    print(X)  # 2
    print(L)  # [3,4]
    print('')

    X, D = multiple(X, D)  # assignment overwrites previous values of X and D
    print(X)  # 2
    print(D)  # [3,4]
    print('')

    X, T = multiple(X, T)  # assignment overwrites previous values of X and T
    print(X)
    print(T)
    print('')

    Y = 2
    print(Y)  # 2
    print('')

    X, Y = multiple(X, Y)  # assignment overwrites previous values of X and Y

    print(X)  # 2
    print(Y)  # [3,4]

