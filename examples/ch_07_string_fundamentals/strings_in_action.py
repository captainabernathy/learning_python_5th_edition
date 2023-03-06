if __name__ == '__main__':
    print('code snippets from pages 206-215\n')
    # basic operations
    print(len('abc'))  # 3
    print('abc' + 'def')  # abcdef... concatenation
    print('Ni!' * 4)  # Ni! 4 times... repetition
    print('-' * 80)  # 80 dashes... repetition
    print('')

    # iteration
    myjob = 'hacker'
    for c in myjob:
        print(c, end=' ')  # h a c k e r
    print('\n')

    print('k' in myjob)  # True search
    print('z' in myjob)  # False
    print('spam' in 'abcspamdef')  # True
    print('')

    # indexing and slicing
    S = 'spam'
    print(S[0], S[-2])  # s,  a
    print(S[1:3], S[1:], S[:-1])  # pa, pam, spa
    print('')

    S = 'abcdefghijklmnop'
    print(S[1:10:2])  # bdfhj... from element 1 to element 10 by 2
    print(S[::2])  # acegikmo every other character
    print('')

    S = 'hello'
    # reverse string
    print(S[::-1])  # olleh... from the end to the beginning

    S = 'abcdefg'
    # substring reverse
    print(S[5:1:-1])  # fedc... from element 5 to element 1
    print('')

    # slice literal
    print('spam'[1:3])  # pa
    # slicing with a slice object
    print('spam'[slice(1, 3)])  # pa
    print('')
    print('spam'[::-1])  # maps
    print('spam'[slice(None, None, -1)])  # maps
    print('')

    # string conversion
    # NOTE: repr() returns the as-code representation of its input as a string
    print(int("42"), str(42), repr(42))  # 42 42 42
    print(str('spam'), repr('spam'))  # spam, 'spam'

    S = "42"
    It = 1
    print(S, It)  # 42, 1
    print(int(S) + It)  # 42
    print(S + str(It))   # 421
    print(str(3.1415), float("1.5"))  # 3.1415, 1.5

    t = "1.234E-10"
    print(float(t))  # 1.234e-10
    print('')

    # character code conversions
    # NOTE: ord() returns the binary value used to represent the corresponding
    # character in memory
    print(ord('s'))  # 115

    # NOTE: chr() returns the character corresponding to the integer code it
    # receives
    print(chr(115))  # s

    S = '5'
    print(S)  # 5
    S = chr(ord(S) + 1)
    print(S)  # 6
    print(int('5'))  # 5
    print(ord('5') - ord('0'))  # 5
    print('')

    # convert binary digits to integer with ord
    # 0 x 2 + (1) = 1
    # 1 * 2 + (1) = 3
    # 3 * 2 + (0) = 6
    # 6 * 2 + (1) = 13
    B = '1101'
    It = 0
    while B != '':
        It = It * 2 + (ord(B[0]) - ord('0'))
        B = B[1:]  # advance B to start with the next  digit in the string

    print(It)  # 13
    print(int('1101', 2))  # 13... convert binary to integer: built-in
    print(bin(13))  # 0b1101... convert integer to binary: built-in
    print('')

    # changing strings
    S = 'spam'
    print(S)  # spam

    # to change a string make a new one
    S = S + 'SPAM!'  # concatenation
    print(S)  # spamSPAM

    S = S[:4] + 'Burger' + S[-1]  # concatenation
    print(S)  # spamBurger!

    S = 'splot'
    S = S.replace('pl', 'pamal')  # string replace() method
    print(S)  # spamalot
    print('')

    # string formatting expression
    print('That is %d %s bird!' % (1, 'dead'))
    # string format method
    print('That is {0} {1} bird!'.format(1, 'dead'))
