from __future__ import print_function
from rangetest import rangetest


@rangetest(age=(0, 120))
def person_info(name, age):
    # person_info = rangetest(age=(0, 120))(person_info)
    print('%s is %s years old' % (name, age))


@rangetest(M=(1, 12), D=(1, 31), Y=(0, 2013))
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))


class Person:
    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

    @rangetest(percent=(0.0, 1.0))
    def give_raise(self, percent):
        # give_raise = give_raise(percent=(0.0, 1.0))(give_raise)
        self.pay = int(self.pay * (1 + percent))


@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)


if __name__ == '__main__':
    print('code snippets from pages 1380-1382\n')

    person_info('Bob', 40)  # Bob is 40 years old
    print('')

    person_info(age=40, name='Bob')  # Bob is 40 years old
    print('')

    birthday(5, D=1, Y=1963)  # birthday = 5/1/1963
    print('')

    try:
        person_info('Bob', 150)
    except TypeError as ex:
        print(ex)  # person_info argument "age" not in 0..120
    print('')

    try:
        person_info(age=150, name='Bob')
    except TypeError as ex:
        print(ex)  # person_info argument "age" not in 0..120
    print('')

    try:
        birthday(5, D=40, Y=1963)
    except TypeError as ex:
        print(ex)  # birthday argument "D" not in 1..31
    print('')

    bob = Person('Bob Smith', 'dev', 100000)
    sue = Person('Sue Jones', 'dev', 100000)

    bob.give_raise(0.10)
    sue.give_raise(percent=0.20)

    print(bob.pay)  # 110000
    print(sue.pay)  # 120000
    print('')

    try:
        bob.give_raise(1.10)
    except TypeError as ex:
        print(ex)  # give_raise argument "percent" not in 0.0..1.0
    print('')

    try:
        bob.give_raise(percent=1.20)
    except TypeError as ex:
        print(ex)  # give_raise argument "percent" not in 0.0..1.0
    print('')

    omitargs(1, 2, 3, 4)  # 1 2 3 4
    print('')

    omitargs(1, 2, 3)  # Argument "d" default
    print('')  # 1 2 3 9

    omitargs(1, 2, 3, d=4)  # 1 2 3 4
    print('')

    # Argument "b" defaulted... Argument "c" defaulted... 1 7 8 4
    omitargs(1, d=4)
    print('')

    # Argument "b" defaulted... Argument "c" defaulted... 1 7 8 4
    omitargs(d=4, a=1)
    print('')

    omitargs(1, b=2, d=4)  # Argument "c" defaulted... 1 2 8 4
    print('')

    omitargs(d=8, c=7, a=1)  # Argument "b" defaulted 1 7 7 8
    print('')

    try:
        omitargs(1, 2, 3, 11)
    except TypeError as ex:
        print(ex)  # omitargs argument "d" not in 1..10
    print('')

    try:
        omitargs(1, 2, 11)
    except TypeError as ex:
        print(ex)  # omitargs argument "c" not in 1..10
    print('')

    try:
        omitargs(1, 2, 3, d=11)
    except TypeError as ex:
        print(ex)  # omitargs argument "d" not in 1..10
    print('')

    try:
        omitargs(11, d=4)
    except TypeError as ex:
        print(ex)  # omitargs argument "a" not in 1..10
    print('')

    try:
        omitargs(d=4, a=11)
    except TypeError as ex:
        print(ex)  # omitargs argument "a" not in 1..10
    print('')

    try:
        omitargs(1, b=11, d=4)
    except TypeError as ex:
        print(ex)  # omitargs argument "b" not in 1..10
    print('')

    try:
        omitargs(d=8, c=7, a=11)
    except TypeError as ex:
        print(ex)  # omitargs argument "a" not in 1..10
    print('')

