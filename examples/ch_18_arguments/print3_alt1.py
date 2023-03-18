import sys


# function that emulates most of the functionality fo the python3 print()
# function and can be used with python3 only.
# it supports the following keyword-only arguments only: sep, end, and file
# unexpected keyword arguments will generate an exception
def print3(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''  # start empty
    first = True
    for arg in args:  # loop over arguments
        output += ('' if first else sep) + str(arg)  # build up output string
        first = False
    file.write(output + end)  # write output
