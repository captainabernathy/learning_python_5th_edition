if __name__ == '__main__':
    print('code snippets from pages 156-158\n')
    print(0o1, 0o20, 0o377)  # 1 16 255 (octal)
    print(0x1, 0x10, 0xFF)  # 1 16 255 (hex)
    print(0b1, 0b10000, 0b11111111)  # 1 16 255 (binary)
    print('')

    print(0xFF, (15 * (16 ** 1)) + (15 * (16 ** 0)))  # 255 255
    print(0x2F, (2 * (16 ** 1)) + (15 * (16 ** 0)))  # 47 47
    print(0xF, 0b1111, (1 * (2 ** 3)) + (1 * (2 ** 2)) + (1 * (2 ** 1))
          + (1 * (2 ** 0)))  # 15 15 15
    print('')

    # numbers -> digit strings
    print(oct(64), hex(64), bin(64))  # 0o100 0x40 0b1000000
    print('')

    # digits -> numbers in scripts and strings
    print(64, 0o100, 0x40, 0b1000000)  # 64 64 64 64

    # 64 64 64 64
    print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
    print(int('0x40', 16), int('0b1000000', 2))  # 64 64 literals too
    print('')

    # NOTE: eval() treats as python code... be careful
    # 64 64 64 64
    print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))
    print('')

    # string format() method
    print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))  # 100, 40, 1000000
    # string formatting expression
    print('%o, %x, %x, %X' % (64, 64, 255, 255))  # 100 40 ff FF
    print('')

    X = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    print(X)  # a really big number
    print(oct(X))  # 0o177...7
    print(bin(X))  # 0b1111...1
