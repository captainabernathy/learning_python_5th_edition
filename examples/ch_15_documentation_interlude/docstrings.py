'''
Module documentation
Words Go here
'''

# NOTE: importing a file as a module reloads it
# reloading a file enables inspection of its __doc__ attributes
import docstrings  # reload this file


def square(x):
    '''
function documentation
can w have your liver then?
    '''
    return x ** 2


if __name__ == '__main__':
    print('code snippets from page 465\n')
    print(square(4))
    print(square.__doc__)  # function documentation

    print(docstrings.__doc__)  # module documentation
    print(docstrings.square.__doc__)  # function documentation

    # NOTE: the built-in help function displays the documentation associated
    # with the object it receives in a formatted help page
    help(docstrings.square)
