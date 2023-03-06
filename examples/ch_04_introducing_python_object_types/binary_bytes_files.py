import struct  # module can both create and unpack binary data

if __name__ == '__main__':
    print('code snippets from page 127\n')
    # create packed binary data
    packed = struct.pack('>i4sh', 7, b'spam', 8)
    print(packed)

    # create a binary file
    f = open('data.bin', 'wb')
    f.write(packed)  # write packed binary data
    f.close()  # close file

    # read binary file
    data = open('data.bin', 'rb').read()  # file auto-closed
    print(data)

    print(data[4:8])  # b'spam'

    # a sequence of 8-bit bytes
    print(list(data))  # [0,0,0,7,115,112,97,109,0,8]

    # unpack data into objects
    print(struct.unpack('>i4sh', data))  # (7, b'spam', 8)
