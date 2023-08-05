# usage: python3 division_classic_floor_true.py

import math

if __name__ == '__main__':
    print('code snippets from pages 152-155\n')

    # NOTE: in 2.X / truncates results for integer division towards the floor..
    # in 3.X / always performs floating-point division
    # // performs floor division in 2.X and 3.X
    print(10 / 4)  # differs in 3.X
    print(10 / 4.0)  # same in 3.X
    print(10 // 4)  # same in 3.X (floor division)
    print(10 // 2.0)  # same in 3.X (floor division)
    print('')

    Y = 4
    Z = 6
    X = Y // Z  # always truncates results for ints in 2.X and 3.X
    W = Y / float(Z)  # floor division wih remainder in either 2.X or 3.X
    print(X)  # 0
    print(W)  # 0.66...6
    print('')

    print(math.floor(2.5))  # 2 same in 3.X and 2.X
    print(math.floor(-2.5))  # -3 same in 3.X and 2.X
    print(math.trunc(2.5))  # 2 same in 3.X and 2.X
    print(math.trunc(-2.5))  # -2 same in 3.X and 2.X
    print('')

    print(5 / 2, 5 / -2)  # differs in 3.X (2.5, -2.5) and 2.X (2, -3)
    print(5 // 2, 5 // -2)  # 2, -3 same in 3.X and 2.X
    print(5 / 2.0, 5 / -2.0)  # 2.5, -2.5 same in 3.X and 2.X
    print(5 // 2.0, 5 // -2.0)  # 2.0, -3.0 same in 3.X and 2.X
    print('')

    print(5 / -2)  # -2.5 keep remainder in 3.X, -3 truncated to floor in 2.X;
    print(5 // -2)  # -3... floor below result in 3.X and 2.X
    print(math.trunc(5 / -2))  # -2 in 3.X, -3 in 2.X
    print('')

    print(5 / float(-2))  # -2.5 same in 3.X and 2.X
    print(5 / -2, 5 // -2)  # -2.5, -3 in 3.X, -3, -3 in 2.X
    print(math.trunc(5 / float(-2)))  # -2 in 3.X and 2.X
    print('')

    # 2.5, 2.5, -2.5, -2.5 in 3.X
    #   2, 2.5, -2.5, -3   in 2.X
    print(5 / 2, 5 / 2.0, 5 / -2.0, 5 / -2)

    # 2, 2.0, -3.0, -3 in 3.X
    # 2, 2.0, -3.0, -3 in 2.X (same)
    print(5 // 2, 5 // 2.0, 5 // -2.0, 5 // -2)

    # 3.0, 3.0, 3, 3.0 in 2.X and 3.X
    print(9 / 3, 9.0 / 3, 9 // 3, 9 // 3.0)
