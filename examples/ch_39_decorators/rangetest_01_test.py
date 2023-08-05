# usage: python(2/3) rangetest_01_test.py

from __future__ import print_function
from rangetest_01 import rangetest


# (i,low,high) => range to test
@rangetest((1, 0, 120))
def person_info(name, age):  # person_info = rangetest((1,0,120))(person_info)
    print('%s is %s years old' % (name, age))


# validate M is b/t 1 and 12, D is b/t 1 and 31, Y is b/t 0 and 2009
@rangetest([0, 1, 12], [1, 1, 31], [2, 0, 2009])
def birthday(M, D, Y):  # birthday = rangetest(...)(birthday)
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))


class Person:
    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

    @rangetest([1, 0.0, 1.0])
    def give_raise(self, percent):  # give_raise = rangetest(...)(give_raise)
        self.pay = int(self.pay * (1 + percent))


if __name__ == '__main__':
    print('code snippets from pages 1377- 1379\n')

    person_info('Bob Smith', 45)  # Bob Smith is 45 years old
    print('')

    try:
        person_info('Bob Smith', 200)
    except TypeError as ex:
        print(ex)  # argument 1 not in 0..120
    print('')

    birthday(5, 31, 1963)  # birthday = 5/31/1963
    print('')

    try:
        birthday(5, 32, 1963)
    except TypeError as ex:
        print(ex)  # argument 1 not in 1..31
    print('')

    sue = Person('Sue Jones', 'dev', 100000)

    sue.give_raise(0.10)  # OK
    print(sue.pay)  # 110000
    print('')

    try:
        sue.give_raise(1.10)
    except TypeError as ex:
        print(ex)  # argument 1 not in 0.0..1.0
    print('')
