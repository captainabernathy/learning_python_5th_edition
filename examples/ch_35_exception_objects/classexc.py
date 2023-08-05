# usage: python3 classexc.py

class General(Exception):
    pass


class Specific1(General):
    pass


class Specific2(General):
    pass


def raiser0():
    X = General()
    raise X  # raises superclass instance


def raiser1():
    X = Specific1()
    raise X  # raises subclass instance


def raiser2():
    X = Specific2()
    raise X  # raises subclass instance


if __name__ == '__main__':
    print('code snippets from page 1164\n')

    for func in (raiser0, raiser1, raiser2):
        try:
            func()
        except General:  # match General or any of its subclasses
            import sys
            # sys.exec_info()[0] grabs the most recently raised exception...
            # element 0 is the class of the exception raised
            print('caught: %s' % sys.exc_info()[0])
            # caught: <class '__main__.General'>
            # caught: <class '__main__.Specific1'>
            # caught: <class '__main__.Specific2'>
