# NOTE: the __index__() method in python 3.X returns the integer value for
# instance... and is used by built-ins that convert their argument to numeric
# strings
class C:
    def __index__(self):
        return 255


if __name__ == '__main__':
    print('code snippets from page 922\n')

    X = C()
    print(hex(X))  # 0xff
    print(bin(X))  # 0b11111111
    print(oct(X))  # Oo377
    print('')

    print(('C' * 256)[255])  # C
    print(('C' * 256)[X])  # same result as ^^^ as __index__ (not X[i])
    print(('C' * 256)[X:])  # same result as ^^^... as __index__ (not X[i])
