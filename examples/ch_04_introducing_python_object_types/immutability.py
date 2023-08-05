# usage: python3 immutability.py

if __name__ == '__main__':
    print('code snippets from pages 103-104\n')

    S = 'Spam'
    print(S)  # Spam

    # immutable objects cannot be changed
    # S[0] = 'z'

    # use expression to create new object
    S = 'z' + S[1:]
    print(S)  # zpam

    S = 'shrubbery'
    print(S)  # shrubbery

    # expand S to list
    L = list(S)
    print(L)  # ['s', 'h', ..., 'y']

    # change list in place
    L[1] = 'c'
    print(L)  # ['s', 'c', ..., 'y']

    # join with empty delimiter
    L = ''.join(L)  # converts L to a string
    print(L)  # scrubbery

    # byte array is mutable
    B = bytearray(b'spam')  # 'b' is needed in 3.X

    # use decode() to translate bytearray to string
    print(B.decode())  # spam

    # use extend() to modify bytearray
    B.extend(b'eggs')
    print(B.decode())  # spameggs

    # use ord() to modify an individual character
    B[0] = ord('S')  # change B[0] to S
    print(B.decode())  # Spameggs
