# NOTE: a keyword-only argument is an argument that must be specified by
# keyword and cannot be filled by another positional argument. keyword-only
# arguments must be specified after a *argument and/or before a **argument

# NOTE: a keyword-only argument that does not have a default value, must be
# specifed when the function is called
def kwonly1(a, *b, c):  # c must be specified by keyword
    print(a, b, c)


# NOTE: an empty * parameter specified in a function header indicates that the
# function does not accept a variable lenght argument list. a function header
# cannont include a an empty ** parameter
def kwonly2(a, *, b, c):  # b and c are keyword only arguments
    print(a, b, c)


# NOTE: a keyword-only argument that is provided with a default value, may be
# ommitted when the function is called
def kwonly3(a, *, b='spam', c='ham'):  # keyword-only arguments with defaults
    print(a, b, c)


def kwonly4(a, *, b, c='spam'):  # b must be specified by the caller
    print(a, b, c)


def kwonly5(a, *, b=1, c, d=2):  # c must be specified by the caller
    print(a, b, c, d)


if __name__ == '__main__':
    print('code snippets from pages 559-561\n')
    kwonly1(1, 2, c=3)  # 1 (2,) c=3
    kwonly1(1, *(2,), c=3)  # 1 (2,) 3... same as ^^
    kwonly1(1, 2, 3, c=4)  # 1 (2,3) 4... arguments before c collected into *b
    kwonly1(1, *(2, 3), c=4)  # 1 (2,3) 4... same as ^^
    kwonly1(*(1, 2, 3), c=4)  # 1 (2,3) 4... same as ^^ first arg unpacked to a
    kwonly1(a=1, c=3)  # 1 () 3... b is an empty tuple
    
    # NOTE: c must be named
    try:
        kwonly1(1, 2, 3)  # error... does not name c
    except TypeError as ex:
        print(ex)

    # NOTE a positional argument cannot follow a keyword argument
    # kwonly1(a=1, 2, 3, c=4)
    print('')

    kwonly2(1, c=3, b=2)  # 1 2 3
    kwonly2(c=3, b=2, a=1)  # 1 2 3
    
    # NOTE: be careful not pass more positional arguments to a function than
    # it defines
    try:
        kwonly2(1, 2, 3)  # error... b and c must be named
    except TypeError as ex:
        print(ex)

    try:
        kwonly2(1)  # error... b and c have no defaults
    except TypeError as ex:
        print(ex)
    print('')

    kwonly3(1)  # 1 spam ham... uses defaults for b and c
    kwonly3(a=1)  # 1 spam ham... uses defaults for b and c
    kwonly3(1, b=2)  # 1 2 ham... uses default for c
    kwonly3(1, c=3)  # 1 spam 3... uses default for b

    # NOTE: a must be named when a keyword argument is passed before it
    kwonly3(c=3, b=2, a=1)  # 1 2 3
    kwonly3(c=3, a=1)  # 1 spam 3... uses default for b
    kwonly3(b=2, a=1)  # 1 2 ham... uses defalt for c
   
    # NOTE: be careful not pass more positional arguments to a function than
    # it defines
    try:
        kwonly3(1, 2)  # too many positional args
    except TypeError as ex:
        print(ex)
    print('')

    kwonly4(1, b='eggs')  # 1 eggs spam... uses default for c
    try:
        kwonly4(1, c='eggs')  # error... does not name b and b has no default
    except TypeError as ex:
        print(ex)
    print('')

    kwonly5(3, c=4)  # 3 1 4 2... uses defaults for b and d
    kwonly5(3, c=4, b=5)  # 3 5 4 2... uses default for d
   
    try:
        kwonly5(3)  # error... does not name c and c has no default
    except TypeError as ex:
        print(ex)
