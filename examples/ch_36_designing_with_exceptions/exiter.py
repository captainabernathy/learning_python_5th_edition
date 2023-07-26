import sys


# NOTE: a bare except might unknowingly prevent a crucial exit
def bye():
    sys.exit(40)


if __name__ == '__main__':
    print('code snippets from page 1192\n')

    try:
        bye()
    except:  # bare except prevents exit()
        print('got it')
    print('continuting...\n')

    try:
        bye()
    except Exception:  # does not block exit()
        print('got it')  # not reached
    print('continuing')
