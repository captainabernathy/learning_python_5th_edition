if __name__ == '__main__':
    print('code snippets from pages 1144-1145\n')

    sep = '-' * 45 + '\n\n'

    print(sep + 'EXCEPTION RAISED AND CAUGHT')
    print('')
    try:
        x = 'spam'[99]
    except IndexError:
        print('exception caught')  # runs
    finally:
        print('finally...')  # always runs
    print('moving on...')
    print('')

    print(sep + 'NO EXCEPTION RAISED')
    print('')
    try:
        x = 'spam'[3]
    except IndexError:
        print('exception caught')
    finally:
        print('finally...')  # always runs
    print('moving on...')
    print('')

    print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
    print('')
    try:
        x = 'spam'[3]
    except IndexError:
        print('exception caught')
    else:
        print('else...')  # runs
    finally:
        print('finally...')  # always runs
    print('moving on...')
    print('')

    print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
    print('')
    try:
        x = 1 / 0  # raises ZeroDivisionError
    except IndexError:
        print('exception caught')
    finally:
        print('finally...')  # always runs

    # never runs
    print('moving on...')
    print('')
