# function that returns a handle to a lambda function that will subsequently
# return the value of 4 raised to the power of the value passed to it
def func1():
    x = 4
    action = (lambda n: x ** n)  # use x from enclosing def
    return action  # return handle


# function that returns a handle to a lambda function that will subsequently
# return the value of 4 raised to the power of the value passed to it
def func2():
    x = 4
    # manually pass x with its default value to the lambda function
    action = (lambda n, x=x: x ** n)
    return action


# function that returns a handle to a list of 5 lambda functions. each handle
# will subsequently return the value of the function's position in the list
# by the value of the argument passed to it
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)  # set default i
    return acts


# function that defines and calls a nested function, which also defines
# and calls a nested function
def f11():
    x = 99

    def f22():

        def f33():
            print(x)  # uses f1()'s x
        f33()  # called by f2
    f22()  # called by f1


if __name__ == '__main__':
    print('code snippets from pages 526-528\n')
    x = func1()
    print(x(2))  # 16... 4 ** 2

    x = func2()
    print(x(2))  # 16... 4 ** 2
    print('')

    acts = makeActions()

    print(acts[0](2))  # 0 ** 2
    print(acts[1](2))  # 1 ** 2
    print(acts[2](2))  # 2 ** 2
    print(acts[3](2))  # 3 ** 2
    print(acts[4](2))  # 4 ** 2
    print('')

    f11()  # 99
