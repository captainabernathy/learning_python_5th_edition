import sys

if __name__ == '__main__':
    print('code snippets from pages 466-467\n')

    # output documentation of sys module
    print(sys.__doc__)
    print('')

    # output documentation of for sys module's getrefcount() function
    print(sys.getrefcount.__doc__)
    print('')

    L = [1, 2, 3]
    L1 = L
    L2 = L1
    # NOTE: getrefcount() includes the temporary reference it receives in the
    # count it returns... so the result is typically one more that expected
    print(sys.getrefcount(L))
    print('')

    print(int.__doc__)  # documentation for int() constructor
    print('')

    print(map.__doc__)  # documentation for map() constructor
