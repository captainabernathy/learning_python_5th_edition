# usage: python3 classexc2.py

class General(Exception):
    pass


class Specific1(General):
    pass


class Specific2(General):
    pass


def raiser0():
    raise General()  # raises superclass instance


def raiser1():
    raise Specific1()  # raises subclass instance


def raiser2():
    raise Specific2()  # raises subclass instance


if __name__ == '__main__':
    print('code snippets from page 1165\n')

    for func in (raiser0, raiser1, raiser2):
        try:
            func()
        except General as X:
            print('caught %s' % X.__class__)
            # caught: <class '__main__.General'>
            # caught: <class '__main__.Specific1'>
            # caught: <class '__main__.Specific2'>
