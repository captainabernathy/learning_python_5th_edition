# usage: python3 nestexc.py

def action2():
    print(1 + [])  # generates TypeError


def action1():
    try:
        action2()
    except TypeError:  # most recent matching try
        print('inner try')


def action3():
    try:
        action2()
    except TypeError:
        print('inner try')
        raise TypeError  # re-raises Exception


if __name__ == '__main__':
    print('code snippets from page 1181\n')

    try:
        action1()  # inner try
    except TypeError:  # reaches here only if action1() re-raises the exception
        print('outer try')
    print('')

    try:
        action3()  # inner try
    except TypeError:  # reaches here only if action3() re-raises the exception
        print('outer try')
