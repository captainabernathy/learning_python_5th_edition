# usage: python(2/3) validate_tester2.py module_name

from __future__ import print_function
from validate_tester import loadclass


if __name__ == '__main__':
    print('code snippets from page 1304\n')

    CardHolder = loadclass()
    print('')

    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')

    # for: validate_properties, validate_descriptors1, validate_descriptors2,
    # validate_getattr, validate_getattribute
    # bob: bob_smith 12345*** 40 123 main st
    print('bob:', bob.name, bob.acct, bob.age, bob.addr)
    print('')

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')

    # for: validate_properties, validate_descriptors1, validate_descriptors2,
    # validate_getattr, validate_getattribute
    # sue: sue_jones 45781*** 35 124 main st
    print('sue:', sue.name, sue.acct, sue.age, sue.addr)
    print('')

    # for: validate_properties, validate_descriptors2, validate_getattr,
    # validate_getattribute
    # bob: bob_smith 12345*** 40 123 main st

    # for: validate_descriptors1 (NOTE: descriptor state shared across objects)
    # bob: sue_jones 56781*** 35 123 main st
    print('bob:', bob.name, bob.acct, bob.age, bob.addr)
    print('')
