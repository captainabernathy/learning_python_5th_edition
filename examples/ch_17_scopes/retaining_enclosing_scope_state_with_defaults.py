# usage: python3 retaining_enclosing_scope_state_with_defaults.py

# function that defines and calls a nesetd function that accesses a variable
# defined in the enclosing scope
def f1():
    x = 88

    def f2(x=x):  # remember scope with default
        print(x)
    f2()


# function that passes a local variable to a function that is defined later
def f11():
    x = 88
    f2(x)  # pass x... forward reference


# function that outputs its input
def f2(x):
    print(x)


if __name__ == '__main__':
    print('code snippets from pages 525-526\n')

    f1()  # 88
    f11()  # 88
