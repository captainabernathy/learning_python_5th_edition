# usage: python3 space_and_time_conciseness_expressiveness.py

import math
import random
from permute import permute1
from permute import permute2


if __name__ == '__main__':
    print('code snippets from pages 638-639\n')

    print(math.factorial(10))  # 10! = 3,628,800
    print('')

    seq = list(range(10))
    p1 = permute1(seq)  # slow... builds a list w/3.628M elements of size 10
    print(len(p1), p1[0], p1[1])
    print('')

    p2 = permute2(seq)  # generator returns immediately
    print(next(p2))  # next result computed on demand
    print(next(p2))
    print('')

    # still slow to extract all 3.628M results from generator
    p2 = list(permute2(seq))
    print(p1 == p2)  # True
    print('')

    print(math.factorial(50))  # a very big number
    print('')

    p3 = permute2(list(range(50)))  # generator returns on demand
    print(next(p3))  # get next result quiclky
    print('')

    print(math.factorial(20))  # another big number
    print('')

    seq = list(range(20))  # [0,...,19]
    random.shuffle(seq)  # randomly suffle the sequence
    p = permute2(seq)
    print(next(p))  # get a random permutation
    print('')

    random.shuffle(seq)  # shuffle the sequence again
    p = permute2(seq)
    print(next(p))  # get another random permutation
    print(next(p))  # get one of the remaning permutations
