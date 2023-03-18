# NOTE: the program can be run with python 2.X or 3.X
import sys
from print3 import print3

if __name__ == '__main__':
    print('code snippets from pages 568-569\n')
    print3(1, 2, 3)  # 1 2 3
    print3(1, 2, 3, sep='')  # 123
    print3(1, 2, 3, sep='...')  # 1...2...3
    print3(1, [2], (3,), sep='...')  # 1...[2]...(3,)
    print3(4, 5, 6, sep='', end='')  # 456789... overrides default end so
    print3(7, 8, 9)  # this line prints immediately after ^^^
    print3()

    print3(1, 2, 3, sep='??', end='.\n', file=sys.stderr)  # 1??2??3.
