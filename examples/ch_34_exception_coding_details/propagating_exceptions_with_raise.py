# usage: python3 propagating_exceptions_with_raise.py

if __name__ == '__main__':
    print('code snippets from page 1149\n')

    try:
        raise IndexError('spam')  # Exceptions remember arguments
    except IndexError:
        print('propagating')
        raise  # Reraise/propagate the most recent exception
