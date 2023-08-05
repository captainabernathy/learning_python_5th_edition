# usage: python3 bitwise_operations.py

if __name__ == '__main__':
    print('code snippets from pages 158-160\n')

    x = 1
    print(x)
    print(x << 2)  # 4... left shift (1 * (2 ** 2)) = 4
    print(x | 2)  # 3... 0001 | 0010 = 0011 = 3
    print(x & 1)  # 1... 0001 & 0001 = 0001 = 1
    print('')

    X = 0b0001
    print(X)  # 1
    print(X << 2)  # 4
    print(X | 0b010)  # 3
    print(X & 0b1)  # 1
    print('')

    X = 0xFF
    print(bin(X))  # 0b11111111
    print(bin(X ^ 0b10101010))  # 0b1010101... 11111111 ^ 10101010 = 01010101
    print(int('01010101', 2))  # digits -> number... string to int per base
    print(hex(0b01010101))  # 0x55
    print(hex(85))  # 0x55
    print('')

    X = 99
    # NOTE: X.bit_length() is the same as len(bin(X))-2 the -2 is necessary
    # since bin(X) is prepended by 0b
    print(bin(X), X.bit_length(), len(bin(X)) - 2)  # 0b1100011 7 7
    print(bin(256), (256).bit_length(), len(bin(256)) - 2)  # 0b100000000 9 9
