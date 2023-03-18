import sys


# function that emulates most of the functionality of the python3 print()
# function and can be use with python2 or 3.
# it supports the following keyword arguments: sep, end, and file, but assumes
# that all positional arguments are to be printed, and all keyword are for
# options only... so non-supported or erroneous keyword arguments are
# silently ignored
def print3(*args, **kargs):
    sep = kargs.get('sep', ' ')  # sep defaults to ' '
    end = kargs.get('end', '\n')  # end defaults to '\n'
    file = kargs.get('file', sys.stdout)  # file defaults to sys.stdout
    output = ''  # start empty
    first = True
    for arg in args:  # loop over arguments
        output += ('' if first else sep) + str(arg)  # build up output string
        first = False
    file.write(output + end)  # write output
