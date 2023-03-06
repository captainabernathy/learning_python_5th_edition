if __name__ == '__main__':
    print('code snippets from pages 103-108\n')
    S = 'Spam'
    print(S)  # Spam

    # use find() to find the offset of a substring
    print(S.find('pa'))  # 1

    # use replace() to replace occurrences of a substring with another
    print(S.replace('pa', 'XYZ'))  # SXYZm

    # but S has not changed
    print(S)  # Spam

    # use split() to split a string on a delimiter into a list of substrings
    line = 'aaa,bbb,ccccc,dd'
    print(line)  # aaa,...,dd

    print(line.split(','))  # ['aaa',...,'dd']

    # use upper() to convert a string to upper case
    U = S.upper()
    print(U)  # SPAM

    # use lower() to convert a string to lower case
    L = U.lower()
    print(L)  # spam

    # use isalpha() and isdigit() too test a string's contents
    print(S.isalpha())  # True
    print(S.isdigit())  # False

    line = 'aaa,bbb,ccccc,dd\n'
    print(line)

    # use rstrip() to remove whitespace characters on the right side
    print(line.rstrip())  # \n not included in output

    # combine rstrip() and split()
    print(line.rstrip().split(','))  # ['aaa',...,'dd']

    # string modulo
    print('%s, eggs, and %s' % ('spam', 'SPAM!'))

    # format() method, numbers specified
    print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))

    # format() method without number
    print('{}, eggs, and {}'.format('spam', 'SPAM!'))

    # floating-point formatting
    # comma-separate and round to two places
    print('{:,.2f}'.format(296999.2567))  # 296,999.26

    # round first item to two places
    # right justify second item, and pad with zeros to a width of 5
    print('%.2f | %+05d' % (3.14159, -42))  # 3.14 | -0042

    # string concatenation
    print(S + 'NI!')  # SpamNI!

    # call catenation operator directly
    print(S.__add__('NI!'))  # SpamNI!

    S = 'A\nB\tC'
    print(S)  # string contains escape sequences
    print(len(S))  # 5

    # use ord() to get numeric value from a character
    print(ord('\n'))  # 5

    # '\0' does not terminate a string
    S = 'A\0B\0C'
    print(S)  # ABC
    print(len(S))  # 5

    # embedding quotes
    msg = """
    aaaaaaaaaa
    bbb'''bbbbbbbbbb""bbbbbbb'bbbb
    cccccccccc
    """

    print(msg)
