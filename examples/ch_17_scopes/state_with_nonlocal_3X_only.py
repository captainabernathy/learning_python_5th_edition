# usage: python3 state_with_nonlocal_3X_only.py

# function that returns a handle to a function that accepts an argument and
# uses the nonlocal keyword to update the state of a varaible defined in an
# enclosing scope
def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested


if __name__ == '__main__':
    print('code snippets from pages 533-534\n')

    F = tester(0)  # state visible within closure only
    F('spam')  # spam 0

    F(37)  # 37 1

    G = tester(37)
    G(3)  # 3 37
    G('blah')  # blah 38
