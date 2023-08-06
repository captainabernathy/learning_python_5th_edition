# usage: python3 decoall_meta_any_01.py

from types import FunctionType
from decotools import tracer
# from decotools import timer


# metaclass factor that can be used to apply any decorator to all of a class's
# methods
def decorate_all(decorator):
    class MetaDecorate(type):
        def __new__(meta, classname, supers, classdict):
            for attr, attrval in classdict.items():
                if type(attrval) is FunctionType:
                    classdict[attr] = decorator(attrval)
            return type.__new__(meta, classname, supers, classdict)
    return MetaDecorate


# class Person(metaclass=decorate_all(timer(label='**'))):
# class Person(metaclass=decorate_all(timer())):
class Person(metaclass=decorate_all(tracer)):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def last_name(self):
        return self.name.split()[-1]


if __name__ == '__main__':
    print('code snippets from page 1449\n')

    bob = Person('Bob Smith', 50000)  # call 1 to __init__
    sue = Person('Sue Jones', 100000)  # call 2 to __init__
    print('')

    print(bob.name)  # Bob Smith
    print(sue.name)  # Sue Jones
    print('')

    sue.give_raise(0.10)  # call 1 to give_raise

    print('%0.2f' % sue.pay)  # 110000.00
    print('')

    print(bob.last_name())  # call 1 to last_name... Smith
    print(sue.last_name())  # call 2 to last_name... Jones
    print('')

