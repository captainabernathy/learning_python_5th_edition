# usage: python3 lambda_basics.py

# simple function that returns the sum of its arguments
def func(x, y, z):
    return x + y + z


# NOTE: lambda functions are limited to a single expression
# function that returns a handle to a lambda function
def knights():
    title = 'Sir'
    # action = (lambda x: title + ' ' + x)
    # return action  # return lambda
    return (lambda x: title + ' ' + x)  # same as ^^^


if __name__ == '__main__':
    print('code snippets from page 591\n')

    print(func(2, 3, 4))  # 9
    print('')

    f = (lambda x, y, z: x + y + z)  # same as func() above
    print(f(2, 3, 4))  # 9
    print('')

    # lambda function with default values
    x = (lambda a="fee", b="fie", c="foe": a + b + c)
    print(x())  # feefiefoe
    print(x("wee"))  # weefiefoe... override first argument to lambda, use
                     # use defaults for b and c
    print('')

    act = knights()  # returns a handle to a lambda function
    msg = act('robin')
    print(msg)  # Sir Robin
    print(act)  # <function knights...> a function... not its result
