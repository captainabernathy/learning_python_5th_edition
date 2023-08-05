# usage: python3 state_with_function_attributes_3X_and_2X.py

# function that uses the value it receives to initialize an internal attribute
# and returns a handle to a nested function that update the attribute
def tester1(start):
    def nested(label):
        print(label, nested.state)  # nested in enclosing scope
        nested.state += 1
    nested.state = start  # initial state after function defined
    return nested


# state with mutables
# NOTE: it is possible to change a mutable object in the enclosing scope in
# python 2.X and 3.X without declaring it nonlocal
def tester2(start):
    def nested(label):
        print(label, state[0])
        state[0] += 1
    state = [start]
    return nested


if __name__ == '__main__':
    print('code snippets from pages 537-538\n')

    F = tester1(0)
    F('spam')  # spam 0
    F('ham')  # ham 1
    print(F.state)  # 2... access function attribute directly
    print('')

    G = tester1(42)
    G('eggs')  # eggs 42
    F('ham')  # ham 3
    print(F.state)  # 3
    print(G.state)  # 43
    print(F is G)  # False
    print('')

    F = tester2(0)
    F('spam')  # spam 0
    F('ham')  # ham 1
    print('')

    G = tester2(42)
    G('eggs')  # eggs 42
    F('ham')  # ham 2
