# usage: python3 decoall_manual.py

from decotools import tracer


class Person:
    @tracer
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def last_name(self):
        return self.name.split()[-1]


if __name__ == '__main__':
    print('code snippets from pages 1447-1448\n')

    bob = Person('Bob Smith', 50000)  # call 1 to __init__
    sue = Person('Sue Jones', 100000)  # call 2 to __init__
    print('')

    print(bob.name)  # Bob Smith
    print(sue.name)  # Sue Jones
    print('')

    sue.give_raise(0.10)  # call 1 to give_raise

    print('%.2f' % sue.pay)  # 110000.00
    print('')

    print(bob.last_name())  # call 1 to last_name... Smith
    print('')

    print(sue.last_name())  # call 2 to last_name... Jones
    print('')

