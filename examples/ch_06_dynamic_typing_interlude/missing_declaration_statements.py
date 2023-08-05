# usage: python3 missing_declaration_statements.py

if __name__ == '__main__':
    print('code snippets from pages 182-185\n')

    # assignments in python perform the following:
    #   1.  Create an object to represent the value on the right-hand side
    #   2.  Create a variable with the on the left-hand side if it does not
    #       exist yet
    #   3.  Link the variable on the left-hand side to the object created to
    #       represent the value(s) on the right-hand side

    a = 3  # a is an integer
    print("a:", a)  # 3

    a = 'spam'  # a is now a string... 3 is reclaimed by python
    print("a:", a)  # spam

    a = 1.23  # a is now a double... 'spam' is reclaimed by python
    print("a:", a)  # 1.23

    print('')

    x = 42  # x is an integer
    print("x: ", x)  # 42

    x = 'shrubbery'  # x is now a string... 42 is reclaimed by python
    print("x: ", x)

    x = 3.1415  # x is now a double... 'shrubbery' is reclaimed by python
    print("x: ", x)

    x = [1, 2, 3]  # x is now a list... 3.1415 is reclaimed by python
    print("x: ", x)
