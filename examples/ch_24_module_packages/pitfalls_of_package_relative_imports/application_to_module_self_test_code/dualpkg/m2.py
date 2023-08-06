# from . import m1  # m2 works in package, but can't run m2 as a program
# import m1  # doesn't work in packge, but can run m2 as a program

# NOTE: m2 works in package and can run m2 as a program when the directory
# above this one is on PYTHONPATH
# (ie: export PYTHONPATH='/path/to/dir/above/this/one')

# usage: python3 m2.py

import dualpkg.m1 as m1


def somefunc():
    m1.somefunc()
    print('m2.somefunc')


if __name__ == '__main__':
    somefunc()
