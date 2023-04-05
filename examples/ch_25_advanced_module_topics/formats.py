def commas(N):
    '''
    formats positive number N for display with commas b/t digit groupings
    '''
    digits = str(N)  # covert N to string
    assert(digits.isdigit())  # ensure conversion produced a digit
    res = ''  # start empty
    while digits:
        # remove the last 3 digits from digits and save them in last3
        digits, last3 = digits[:-3], digits[-3:]
        # prepend the result with last3 and a comma if res isn't empty
        # otherwise set the result to last3
        res = (last3 + ',' + res) if res else last3
    return res


def money(N, num_width=0, currency='$'):
    '''
    formats number N for display with commas, 2 decimal digits, leading $ and
    sign... and optional padding
    numw_width = 0 for no padding, use a number less than 0 to add padding to
    the right (N is left justified), or use a number greater than 0 to add
    padding to the left (N is right justified), ()currency='' to omit symbol,
    and non-ASCII for others (pound=u'\xA3' or u'\u00A3')
    '''
    # set sign to the negative sign if N is < 0, otherwise leave it empty
    sign = '-' if N < 0 else ''
    N = abs(N)  # take the absolute value of the number
    # get a comma separated string of the non-decimal digits of N
    whole = commas(int(N))
    # get a string that contains the decimal portion of N rounded to two digits
    fract = ('%.2f' % N)[-2:]
    # get a string that consist of the sign, whole, and fractional parts of N
    num = '%s%s.%s' % (sign, whole, fract)
    # format numeric string with currency symbol and padding
    return '%s%*s' % (currency, num_width, num)


if __name__ == '__main__':
    print('code snippets from pages 776-777\n')

    '''
    Usage: python prog.py num pad or just python prog.py
    '''
    
    # selftest() fun with this module is run as a stand-alone program and
    # no arguments are provided on the command line
    def selftest():
        tests = 0, 1
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))

        print('')
        tests = 0, 1, -1, 1.23, 1., 1.2, 3.14159
        tests += 12.34, 12.344, 12.345, 12.346
        tests += 2 ** 32, (2 ** 32 + .2345)
        tests += 1.2345, 1.2, -0.2345
        tests += -1.2345, -1.2, -0.2345
        tests += -(2 ** 32), -(2 ** 32 + .2345)
        tests += (2 ** 100), -(2 ** 100)
        for test in tests:
            print('%s [%s]' % (money(test,  17), test))

    import sys
    if len(sys.argv) == 1:
        # run selftest() when program name is the only name on the command line
        selftest()
    else:
        # format the first command line argument as money with padding that
        # corresponds to the value of the second command line argument
        print(money(float(sys.argv[1]), int(sys.argv[2])))
