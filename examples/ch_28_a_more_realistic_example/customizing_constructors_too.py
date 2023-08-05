# usage: python3 customizing_constructors_too.py

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=0.10):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    print('code snippets from pages 859-860\n')

    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob)  # [Person: Bob Smith, 0]
    print(sue)  # [Person: Sue Jones, 100000]
    print(bob.last_name(), sue.last_name())  # Smith Jones

    sue.give_raise(.10)
    print(sue)  # [Person: Sue Jones, 110000]

    tom = Manager('Tom Jones', 50000)
    tom.give_raise(0.10)

    print(tom.last_name())  # Jones
    print(tom)  # [Person: Tom Jones, 60000]
