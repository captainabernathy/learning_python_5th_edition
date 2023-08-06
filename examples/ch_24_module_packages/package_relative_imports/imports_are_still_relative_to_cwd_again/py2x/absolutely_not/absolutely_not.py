# usage: python2 absolutely_not.py

# loads string from pkg  (via relative import due to 2.X import rules)
import pkg.spam

# loads string from from this directory (via relative import due to 2.X import
# rules)
import string


if __name__ == '__main__':
    print 'code snippets from pages 752-753\n'

    print string
