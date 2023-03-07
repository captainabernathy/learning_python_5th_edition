if __name__ == '__main__':
    print('code snippets from pages 371-373\n')
    x = 'spam'
    y = 99
    z = ['eggs']
    print(x, y, z)  # spam 99 ['eggs']
    print('')

    # suppress separator
    print(x, y, z, sep='')  # spam99['eggs']
    print('')

    # custom separator
    print(x, y, z, sep=', ')  # spam, 99, ['eggs']
    print('')

    # suppress line break
    print(x, y, z, end='')  # spam 99 ['eggs']spam
    print(x)
    print('')
    
    # custom line end
    print(x, y, z, end='...\n')
    print('')

    # custom separator and line end
    print(x, y, z, sep='...', end='!\n')  # spam...99...['eggs']
    print(x, y, z, end='!\n', sep='...')  # same as ^^^... order doesn't matter
    print('')

    # write output to file with custom separator
    # NOTE: file is auto-closed
    print(x, y, z, sep='...', file=open('data.txt', 'w'))  # print to a file
    print(x, y, z)  # spam 99 ['eggs']... back to stdout
    # read from file
    print(open('data.txt').read())  # spam...99...['eggs']

    # NOTE: a string formatting expression returns a string
    text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
    print(text)  # Result: 3.1416, 00042
    print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))  # same as ^^^
