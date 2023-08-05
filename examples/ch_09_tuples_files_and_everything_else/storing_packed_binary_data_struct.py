# usage: python3 storing_packed_binary_data_struct.py

import struct

if __name__ == '__main__':
    print('code snippets from pages 302-303\n')

    # open/create file for binary output
    F = open('data.bin', 'wb')

    # the struct module's pack() function creates a formattted binary
    # representation of data
    data = struct.pack('>i4sh', 7, b'spam', 8)
    print(data)
    print('')

    F.write(data)  # write binary data to F
    F.close()  # flush output buffer

    F = open('data.bin', 'rb')  # open file for binary input
    data = F.read()  # read binary data
    print(data)
    print('')

    # the struct module's unpack() function creates a python object from
    # formatted binary data
    values = struct.unpack('>i4sh', data)
    print(values)
