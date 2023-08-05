# usage: python3 nested_scope_examples.py

X = 99  # global variable


# function that defines and calls a nested function that access a varaible
# defined in the enclosing scope
def f1():
    X = 88

    def f2():
        print(X)  # output enclosing def's X
    f2()


# function that returns a handle to a nested function that when subseqently
# called access a variable defined in the enclosing scope
def f1A():
    X = 88

    def f2():
        print(X)  # output enclosing def's X
    return f2  # return handle


if __name__ == '__main__':
    print('code snippets from pages 521-522\n')

    f1()  # 88
    print('')
    action = f1A()
    action()  # 88... calls function f2() nested in f1A()
