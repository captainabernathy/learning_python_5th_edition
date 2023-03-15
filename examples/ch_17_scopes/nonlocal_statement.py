def tester1(start):
    state = start  # referencing nonlocals works normally

    def nested(label):
        print(label, state)  # remembers state in enclosing scope
    return nested


# NOTE: the nonlocal keyword restricts scope lookups to enclosing defs. in
# order to use the nonlocal keyword to lookup a variable in an enclosing def,
# the variable must be already defined in an enclosing scope... the nonlocal
# keyword cannot be used to create a variable that has not been defined in an
# enclosing scope
def tester2(start):
    state = start

    def nested(label):
        # NOTE: updating a variable defined within an enclosing def is
        # not allowed by default/without the nonlocal keyword in 3.X and never
        # allowed in 2.X
        nonlocal state
        print(label, state)
        state += 1  # updates state variable
    return nested


if __name__ == '__main__':
    print('code snippets from pages 531-532\n')
    F = tester1(0)
    F('spam')  # spam 0
    F('ham')  # ham 0
    print('')

    F = tester2(0)
    F('spam')  # spam 0
    F('ham')  # ham 1
    F('eggs')  # eggs 2
    print('')

    G = tester2(42)
    G('spam')  # spam 42
    G('eggs')  # eggs 43
    F('bacon')  # bacon 3
