import traceback


def inverse(x):
    return 1 / x


if __name__ == '__main__':
    print('code snippets from pages 1189-1190\n')

    try:
        inverse(0)
    except Exception:
        # NOTE: uses the traceback module's print_exec() function to write
        # exception info to a file
        traceback.print_exc(file=open('badly.txt', 'w'))
    print('Bye')
