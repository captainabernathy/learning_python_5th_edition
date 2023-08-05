# usage: python3 pydoc_help_function.py

import docstrings
import sys

if __name__ == '__main__':
    print('code snippets from pages 467-470\n')

    # NOTE: use the built-in help() function to display formatted documentation
    # for modules and objects that include docstrings
    help(sys.getrefcount)  # sys module's getrefcount() function
    help(sys)  # sys module
    help(dict)  # dict class
    help(str.replace)  # string replace() method
    help(''.replace)  # replace() method of string instance
    help(ord)  # ord() function
    help(docstrings)  # our docstrings module
