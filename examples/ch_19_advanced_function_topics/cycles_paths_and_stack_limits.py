# usage: python3 cycles_paths_and_stack_limits.py

import sys

if __name__ == '__main__':
    print('code snippets from page 583\n')

    print(sys.getrecursionlimit())  # default limit of recursive calls
    # print(sys.setrecursionlimit(10000))  # setting recursion limit
    help(sys.setrecursionlimit)
