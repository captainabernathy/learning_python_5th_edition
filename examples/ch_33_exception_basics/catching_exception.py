# usage: python3 catching_exception.py

from fetcher import fetcher


def catcher(x):
    try:
        print(fetcher(x, 4))
    except IndexError:
        print('caught exception')
    print('continuing')


if __name__ == '__main__':
    print('code snippets from page 1123\n')

    x = 'spam'
    print(fetcher(x, 3))  # m
    print('')

    try:
        print(fetcher(x, 4))  # past the end... throws exception
    except IndexError:
        print('caught exception')
    print('')

    catcher(x)  # caught exception... continuing
    print('')
