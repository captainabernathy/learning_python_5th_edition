if __name__ == '__main__':
    print('code snippets from page 1149\n')

    try:
        raise IndexError('spam')  # Exceptions remember arguments
    except IndexError:
        print('propagating')
        raise  # Reraise/propagate the most recent exception
