if __name__ == '__main__':
    print('code snippets from pages 1235-1236\n')

    B = b'spam'
    print(B)  # b'spam'
    print('')

    print(list(B))  # [115,112,97,109]... displays integer code point values
    print('')

    C = bytearray(b'xYamLMNO')
    print(C)  # bytearray(b'xYamLMNO')
    print('')

    print(list(C))  # [120,89,97,109,76,77,78,79]... integer code point values
    print('')

    S = 'spam'
    print(S)  # spam
    print('')

    print(list(S))  # ['s','p','a','m']... list of characters
    print('')
