if __name__ == '__main__':
    print('code snippets from pages 442-443\n')
    f = open('script2.py')
    # NOTE: a file object's readlines() method loads a file into a list of
    # strings all at once
    lines = f.readlines()
    f.close()

    print(lines)
    print('')

    # NOTE: a string object's rstrip() method removes whitespace characters on
    # the right side of a string
    lines = [line.rstrip() for line in lines]
    print(lines)
    print('')

    # NOTE: file handle objects are autoclosed when used in a list
    # comprehension
    lines = [line.rstrip() for line in open('script2.py')]
    print(lines)
    print('')

    # convert each line in a file to uppercase
    print([line.upper() for line in open('script2.py')])
    print('')

    # convert each line in a file to uppercase and strip whitespace on the
    # right side
    print([line.rstrip().upper() for line in open('script2.py')])
    print('')

    # split each line in a file into a list of words
    print([line.split() for line in open('script2.py')])
    print('')

    # replace each space in a file with an exclamation point
    print([line.replace(' ', '!') for line in open('script2.py')])
    print('')

    # print whether a line contains 'sys' and the first 5 characters in a line
    # for each line in a file
    print([('sys' in line, line[:5]) for line in open('script2.py')])
