# usage: python3 person.py

from classtools import AttrDisplay


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    print('code snippets from page 863\n')

    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob)  # [Person: job=None, name=Bob Smith, pay=0]
                # call's AttrDisplay's __repr__
    print(sue)  # [Person: job=dev, name=Sue Jones, pay=100000]
                # call's AttrDisplay's __repr__
    print(bob.last_name(), sue.last_name())  # Smith Jones

    sue.give_raise(.10)
    print(sue)  # [Person: job=dev, name=Sue Jones, pay=110000]
                # call's AttrDisplay's __repr__

    tom = Manager('Tom Jones', 50000)
    tom.give_raise(.10)

    print(tom.last_name())  # Jones
    print(tom)  # [Person: job=mgr, name=Tom Jones, pay=60000]
                # call's AttrDisplay's __repr__

