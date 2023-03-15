# function exports a variable to the modlule's global scope and returns a
# handle to a function that accesses and updates this variable
def tester(start):
    # NOTE: use the global keyword to export a variable into the module's
    # global scope from this scope
    global state  # defines state in module's scope
    state = start

    def nested(label):
        # NOTE: in order to access a variable defined within the module's
        # global scope it is necessay to use the global keyword
        global state
        print(label, state)
        state += 1
    return nested


if __name__ == '__main__':
    print('code snippets from pages 534-535\n')
    F = tester(0)  # sets the global state
    F('spam')  # spam 0
    F('eggs')  # eggs 1
    print('')

    G = tester(42)  # updates the global state
    G('toast')  # toast 42
    G('bacon')  # bacon 43
    F('ham')  # ham 44...  reflects the changes made above
