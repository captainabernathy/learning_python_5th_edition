if __name__ == '__main__':
    print('code snippets from page 1231\n')

    # NOTE: indexing a bytes object returns an integer giving the byte's binary
    # value
    B = b'spam'
    print(B)  # b'spam'
    print('')

    print(B[0])  # 115... indexing yields an int
    print(B[-1])  # 109... last byte
    print('')

    print(chr(B[0]))  # s... show character from int
    print('')

    print(list(B))  # [115,112,97,109]... show all bytes
    print('')

    print(B[1:], B[:-1])  # b'pam, b'spa
    print('')

    print(len(B))  # 4
    print('')

    print(B + b'lm')  # b'spamlm'... concatenation
    print('')

    print(B * 4)  # b'spamspamspamspam'... repetition
    print('')
