import struct
from struct import pack


if __name__ == '__main__':
    print('code snippets from pages 1248-1250\n')

    # NOTE: the format string >i4sh means
    # 1) > use big endian byte formatting
    # 2) i4 means a 4-byte integer
    # 3) s means followed by a char array
    # 4) h means followed by a short
    print(pack('>i4sh', 7, b'spam', 8))  # b'\x00\x00\x00\x07spam\x00\x08'
    print('')

    B = struct.pack('>i4sh', 7, b'spam', 8)
    print(B)  # b'\x00\x00\x00\x07spam\x00\x08'
    print('')

    vals = struct.unpack('>i4sh', B)
    print(vals)  # (7,b'spam',8)
    print('')

    try:
        vals = struct.unpack('>i4sh', B.decode())
        print(vals)
    except TypeError as ex:
        print(ex)  # a bytes-like object is required, not 'str'... in 3X
    print('')

    # write values to a packed binary file
    F = open('data.bin', 'wb')  # open file for binary output
    data = struct.pack('>i4sh', 7, b'spam', 8)  # create packed binary data
    print(data)  # b'\x00\x00\x00\x07spam\x00\x08'
    print(F.write(data))  # 10... bytes written to file
    F.close()
    print('')

    # read values from a packed binary fine
    F = open('data.bin', 'rb')
    data = F.read()
    print(data)  # b'\x00\x00\x00\x07spam\x00\x08'

    values = struct.unpack('>i4sh', data)
    print(values)  # (7, b'spam', 8)
    print('')

    # accessing bits of parsed integers
    print(values[0])  # 7... get bits in ints
    print(values[0] & 0x01)  # 1... test first (lowest) bit in int
    print(values[0] | 0b1010)  # 15... bitwise or... turn bits on
    print(bin(values[0] | 0b1010))  # 0b1111
    print(bin(values[0] ^ 0b1010))  # 0b1101
    print(bool(values[0] & 0b100))  # test if bit 3 is set
    print(bool(values[0] & 0b1000))  # test if bit 4 is set
    print('')

    print(values[1])  # b'spam' bytes string... sequence of ints
    print(values[1][0])  # 115
    print(values[1][1:])  # b'pam'... prints as ASCII characters
    print(bin(values[1][0]))  # bits of bytes in strings
    print(bin(values[1][0] | 0b1100))  # turn bits on
    print(values[1][0] | 0b1100)  # 127
    print(values[1].decode())  # spam... decode bytes to string
    print('')
