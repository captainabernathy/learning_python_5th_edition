def raise1():
    raise IndexError


def noraise():
    return


def raise2():
    raise SyntaxError


if __name__ == '__main__':
    print('code snippets from pages 1182-1183\n')

    for func in (raise1, noraise, raise2):
        print('<%s>' % func.__name__)
        try:
            try:
                func()
            except IndexError:  # when func == raise1
                print('caught IndexError')
            except SyntaxError:  # when func == raise2
                print('caught SyntaxError')
        finally:  # runs regardless if there is an exception
            print('finally run')
        print('...')
    print('')

    for func in (raise1, noraise, raise2):
        print('<%s>' % func.__name__)
        try:
            try:
                func()
            except IndexError:  # when func == raise1
                print('caught IndexError')
        except SyntaxError:  # when func == raise2
            print('caught SyntaxError')
        finally:  # runs regardless if there is an exception
            print('finally run')
        print('...')
    print('')
    
    for func in (raise1, noraise, raise2):
        print('<%s>' % func.__name__)
        try:
            func()
        except IndexError:  # when func == raise1
            print('caught IndexError')
        except SyntaxError:  # when func == raise2
            print('caught SyntaxError')
        finally:  # runs regardless if there is an exception
            print('finally run')
            print('...')
