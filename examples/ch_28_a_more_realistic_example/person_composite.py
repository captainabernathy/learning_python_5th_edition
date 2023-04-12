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
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager:
    def __init__(self, name, pay):
        # Manager has a Person attribute
        self.person = Person(name, 'mgr', pay)  # embed a person object

    def give_raise(self, percent, bonus=.10):
        self.person.give_raise(percent + bonus)  # intercept and delegate

    # NOTE: __getattr__() intercepts undefined attribute fetches
    def __getattr__(self, attr):
        return getattr(self.person, attr)  # delegate all other attributes

    # NOTE: in python 3.X, overloaded operators are not routed through 
    # __getattr__() or __getattribute__()
    def __repr__(self):
        return str(self.person)  # must overload again in 3.X


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob)  # [Person: Bob Smith, 0]
    print(sue)  # [Person: Sue Jones, 100000]
    print(bob.last_name(), sue.last_name())  # Smith Jones

    sue.give_raise(.10)
    print(sue)  # [Person: Sue Jones, 110000]

    tom = Manager('Tom Jones', 50000)
    tom.give_raise(.10)

    print(tom.last_name())  # Jones... routed through Person via __getattr__()
    print(tom)  # [Person: Tom Jones, 60000]
    print(tom.person)  # [Person: Tom Jones, 60000]... 
                       # invokes Person's __repr__()
