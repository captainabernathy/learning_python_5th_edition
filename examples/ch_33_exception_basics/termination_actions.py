from fetcher import fetcher


def after(x):
    try:
        fetcher(x, 4)
    except IndexError:
        print('caught exception')
    finally:
        print('after fetch')
    print('after try')


if __name__ == '__main__':
    print('code snippets from pages 1125-1126\n')
    x = 'spam'
    try:
        print(fetcher(x, 3))  # m
    finally:
        print('after fetcher')  # always runs
    print('')

    after(x)  # caught exception, after fetch, after try
    print('')
