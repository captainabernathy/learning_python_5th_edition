# usage: python(2/3) validate_tester.py module_name

from __future__ import print_function


def loadclass():
    import sys
    import importlib
    modulename = sys.argv[1]
    module = importlib.import_module(modulename)  # import via name string
    print('[Using: %s]' % module.CardHolder)
    return module.CardHolder


def printholder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')


if __name__ == '__main__':
    print('code snippets from page 1301\n')

    CardHolder = loadclass()
    print('')

    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')

    # for: validate_properties, validate_descriptors1, validate_descriptors2,
    # validate_getattr, validate_getattribute
    # 12345*** / bob_smith / 40 / 19.5 / 123 main st
    printholder(bob)
    print('')

    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'

    # for: validate_properties, validate_descriptors1, validate_descriptors2,
    # validate_getattr, validate_getattribute
    # 23456*** / bob_q._smith / 50 / 9.5 / 123 main st
    printholder(bob)
    print('')

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')

    # for: validate_properties, validate_descriptors1, validate_descriptors2,
    # validate_getattr, validate_getattribute
    # 56781*** / sue_jones / 35 / 24.5 / 124 main st
    printholder(sue)
    print('')

    # for: validate_properties, validate_descriptors2, validate_getattr
    # validate_getattribute
    # 23456*** / bob_q._smith / 50 / 9.5 / 123 main st

    # for: validate_descriptors1 (NOTE: descriptor state shared across objects)
    # 56781*** / sue_jones / 35 / 24.5 / 124 main st
    printholder(bob)
    print('')

    try:
        sue.age = 200
    except ValueError:
        # for: validate_properties, validate_descriptors1,
        # validate_descriptors2, validate_getattr, validate_getattribute
        print('Bad age for Sue')  # Bad age for Sue
    print('')

    try:
        sue.remain = 5
    except AttributeError:
        # for: validate_properties
        # Can't set sue.remain

        # for: validate_descriptors1, validate_descriptors2, validate_getattr,
        # validate_getattribute
        # cannot set remain
        print('Can\'t set sue.remain')
    except TypeError as ex:
        print(ex)
    print('')

    try:
        sue.acct = '1234567'
    except TypeError:
        # for: validate_properties, validate_descriptors1,
        # validate_descriptors2, validate_getattr, validate_getattribute
        print('Bad acct for Sue')  # Bad acct for Sue
    print('')
