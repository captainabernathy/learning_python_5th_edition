# usage: python3 kaboom.py

def kaboom(x, y):
    print(x + y)  # might trigger TypeError


if __name__ == '__main__':
    print('code snippets from pages 1138-1139\n')

    try:
        kaboom([0, 1, 2], 'spam')  # throws TypeError
    except TypeError:
        print('caught exception')
    print('resuming here')
