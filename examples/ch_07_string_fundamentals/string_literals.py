# usage: python3 string_literals.py
if __name__ == '__main__':
    print('code snippets from pages 199-205\n')

    # string literals can be contained in single or double quotes
    print('shrubbery', "shrubbery")  # shrubbery, shrubbery
    print('')

    # double quotes are embedded in a string encolsed by single quotes, and
    # single quotes are embedded in a string enclosed by double quotes
    print('knight"s', "knight's")
    print('')

    # NOTE: python automatically concatenates adjacent string literals in ANY
    # expression
    title = "Meaning " 'of' " Life"  # implicit concatenation
    print(title)  # Meaning of Life
    print('')

    # to include single quotes in a string enclosed by single quotes, it's
    # necessary to escape them... to include double quotes in a string enclosed
    # by double quotes, it's necessary to escape them
    print('knight\'s', "knight\"s")  # knight's knight"s
    print('')

    s = 'a\nb\tc'  # a string may contain embedded whitespace characters
    print(s)
    print(len(s))  # 5... counts the escaped characters
    print('')

    # NOTE: a null character does not terminate a string the same way that a
    # null byte does in C
    s = 'a\0b\0c'  # a string may contain null characters
    print(s)  # abc
    print(len(s))  # 5... counts the embedded binary zeros
    print('')

    s = '\001\002\x03'
    print(s)  # not printable characters
    print(len(s))  # 3
    print('')

    s = 's\tp\na\x00m'
    print(s)
    print(len(s))  # 7
    print('')

    # raw strings
    # there is no need to escape raw backslahes in raw strings
    path = r'C:\new\text.dat'
    print(path)
    print(len(path))  # 15
    print('')

    # block strings... python collects all triple-quoted text into a single
    # multiline strings that retain all of the enclosed text... whitespace
    # characters included
    mantra = '''Always look
        on the bright
    side of life.'''
    print(mantra)
    print('')

    menu = '''spam      # comments here added to string!
    eggs                # ditto
    '''
    print(menu)  # comments retained in output
    print('')

    # tuple of strings
    menu = (
            "spam\n"  # comments here ignored
            "eggs\n"  # but new lines are not automatic
    )
    print(menu)
