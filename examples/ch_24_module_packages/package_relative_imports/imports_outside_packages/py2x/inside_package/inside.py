# usage: python2 inside.py

# NOTE: imports are relaive to the home directory you're working in, and
# package relative import synatx is not allowed in code that is not in a file
# that ix being used as part of a package
# from . import string  # ERROR
import string  # imports string module in this package

if __name__ == '__main__':
    print 'code snippets from page 748\n'

    print string   # <module 'string' from 'pwd/string.py'>
