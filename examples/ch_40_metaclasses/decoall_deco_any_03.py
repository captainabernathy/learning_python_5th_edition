# usage: python3 decoall_deco_any_03.py

from types import FunctionType
from decotools import tracer, timer


# class decorator factory that can apply any decorator to all of a class's
# methods
def decorate_all(decorator):
    def deco_decorate(acls):
        for attr, attrval in acls.__dict__.items():
            if type(attrval) is FunctionType:
                setattr(acls, attr, decorator(attrval))
        return acls
    return deco_decorate


@decorate_all(timer(label='@@'))
@decorate_all(tracer)
class Person:  # Person = decorate_all(tracer)(Person)
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def last_name(self):
        return self.name.split()[-1]


if __name__ == '__main__':
    print('code snippets from pages 1451-1452\n')

    bob = Person('Bob Smith', 50000)  # call 1 to __init__
    sue = Person('Sue Jones', 100000)  # call 2 to __init__
    print('%0.10f' % Person.__init__.alltime)
    print('')

    print(bob.name)  # Bob Smith
    print(sue.name)  # Sue Jones
    print('')

    sue.give_raise(0.10)  # call 1 to give_raise

    print('%0.2f' % sue.pay)  # 110000.00
    print('%0.10f' % Person.give_raise.alltime)
    print('')

    print(bob.last_name())  # call 1 to last_name... Smith
    print(sue.last_name())  # call 2 to last_name... Jones
    print('%0.10f' % Person.last_name.alltime)
    print('')


