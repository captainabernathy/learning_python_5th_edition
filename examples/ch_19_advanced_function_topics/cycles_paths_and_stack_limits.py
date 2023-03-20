import sys

if __name__ == '__main__':
    print(sys.getrecursionlimit())  # default limit of recursive calls
    # print(sys.setrecursionlimit(10000))  # setting recursion limit
    help(sys.setrecursionlimit)
