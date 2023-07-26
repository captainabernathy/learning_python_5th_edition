def action2():
    print(1 + [])  # generates TypeError


def action1():
    try:
        action2()
    except TypeError:  # most recent matching try
        print('inner try')


if __name__ == '__main__':
    print('code snippets from page 1181\n')

    try:
        try:
            action2()
        except TypeError:
            print('inner try')  # runs
    except TypeError:  # reaches here only if TypeError is re-raised
        print('outer try')
    print('')

    try:
        try:
            action2()
        except TypeError:
            print('inner try')  # runs
            raise TypeError
    except TypeError:  # reaches here only if TypeError is re-raised
        print('outer try')
