import sys


# function that emulates most of the functionality fo the python3 print()
# function and can be used with python3 or 2
# it supports the following keyword arguments only: sep, end, and file
# unexpected keyword arguments will generate an exception
def print3(*args, **kargs):
    sep = kargs.pop('sep', ' ')  # sep defaults to ' '
    end = kargs.pop('end', '\n')  # end defaults to '\n'
    file = kargs.pop('file', sys.stdout)  # file defaults to sys.stdout

    if kargs:  # raise exception for unexpected keyword arguments
        raise TypeError('extra keywords: %s' % kargs)

    output = ''  # start empty
    first = True

    for arg in args:  # loop over arguments
        output += ('' if first else sep) + str(arg)  # build up output string
        first = False
    file.write(output + end)  # write output
