# usage: python3 multiple_vs_single_pass_iterators.py

if __name__ == '__main__':
    print('code snippets from page 455\n')

    R = range(3)  # range allows multiple iterators
    # NOTE: a range object itself is not iterable
    try:
        print(next(R))
    except TypeError as ex:
        print(ex)
    print('')

    # NOTE: range object support multiple iterators
    I1 = iter(R)
    I2 = iter(R)
    print(I1 == R, I2 == R, I1 == I2)  # False False False
    print(next(I1))  # 0
    print(next(I1))  # 1
    print(next(I2))  # 0
    print(next(I1))  # 2
    print('')

    # NOTE: zip and map objects do NOT support multiple iterators
    Z = zip((1, 2, 3), (10, 11, 12))
    I1 = iter(Z)
    I2 = iter(Z)
    print(I1 == Z, I2 == Z, I1 == I2)  # True True True
    print(next(Z))  # (1,10)
    print(next(I2))  # (2,11)
    print(next(I1))  # (3,12)
    print('')

    M = map(abs, (-1, 0, 1))
    I1 = iter(M)
    I2 = iter(M)
    print(I1 == M, I2 == M, I1 == I2)  # True True True
    print(next(M), next(I2), next(I1))  # 1 0 1
    print('')

    R = range(3)
    I1, I2 = iter(R), iter(R)
    print(next(I1), next(I2), next(I1))  # 0 0 1
    print(next(I2))  # 1
