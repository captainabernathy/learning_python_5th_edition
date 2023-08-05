# usage: python3 raising_exceptions.py

if __name__ == '__main__':
    print('code snippets from page 1124\n')

    try:
        raise IndexError
    except IndexError:
        print('caught exception')
