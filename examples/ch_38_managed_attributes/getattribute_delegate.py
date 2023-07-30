# NOTE: delegation-based classes must redefine some operator overloading
# methods (ie: __repr__, __str__) to route them to embedded objects in 3X, but
# NOT in 2X (unless new-style classes are used)

# NOTE: like __getattr__(), __getattribute__() is not run on implicit calls to
# built-in operators in Python 2X and 3X

class Person:
    # constructor builds a Person with its name, job, and pay attributes
    # initialized to name, job, and pay respectively
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    # returns the last string in this Person's name attribute
    def last_name(self):
        return self.name.split()[-1]

    # updates this Person's pay attribute by percent
    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # returns a string representation of this Person
    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager1(object):
    # constructor builds a Manager1 with its person attribute initialized
    # to name, 'mgr', and pay
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)  # embedded person object

    # updates this Manager1's person attribute's pay by percent + bonus
    def give_raise(self, percent, bonus=0.10):
        self.person.give_raise(percent + bonus)  # intercept and delegate

    # returns the string representation of this Manager1 through the string
    # representation of its person attribute
    def __repr__(self):
        return str(self.person)  # overload here required in 3.X

    # returns accesses to this Manager1's person and give_raise attributes
    # throgh object and accesses to other attributes through this Manager1's
    # person attribute
    def __getattribute__(self, attr):
        print('**', attr)
        if attr in ['person', 'give_raise']:
            return object.__getattribute__(self, attr)  # fetch my attrs
        else:
            return getattr(self.person, attr)  # delegate all others


# same as Manager1 except without a __repr__() method
class Manager2(object):
    # constructor builds a Manager2 with its person attribute initialized
    # to name, 'mgr', and pay
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)  # embedded person object

    # updates this Manager2's person attribute's pay by percent + bonus
    def give_raise(self, percent, bonus=0.10):
        self.person.give_raise(percent + bonus)  # intercept and delegate

    # returns accesses to this Manager2's person and give_raise attributes
    # throgh object and accesses to other attributes through this Manager1's
    # person attribute
    def __getattribute__(self, attr):
        print('**', attr)
        if attr in ['person', 'give_raise']:
            return object.__getattribute__(self, attr)  # fetch my attrs
        else:
            return getattr(self.person, attr)  # delegate all others


class Manager3(object):
    # constructor builds a Manager3 with its person attribute initialized
    # to name, 'mgr', and pay
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)  # embedded person object

    # returns accesses to this Manager3's person and give_raise attributes
    # throgh object and accesses to other attributes through this Manager1's
    # person attribute
    def __getattribute__(self, attr):
        print('**', attr)
        person = object.__getattribute__(self, 'person')
        if attr == 'give_raise':
            return lambda percent: person.give_raise(percent + 0.10)
        else:
            return getattr(person, attr)

    # returns the string representation of this Manager3 through the string
    # representation of its person attribute through object
    def __repr__(self):
        # person = object.__getattribute__(self, 'person')
        # return str(person)
        return str(object.__getattribute__(self, 'person'))


if __name__ == '__main__':
    print('code snippets from pages 1297-1298\n')

    sue = Person('Sue Jones', job='dev', pay=100000)
    print(sue.last_name())  # Jones... same as Person.last_name(sue)
    print('')

    sue.give_raise(.10)  # Person.give_raise(sue, 0.10)
    print(sue)  # [Person: Sue Jones, 110000]... same as Person.__repr__(sue)
    print('')

    tom = Manager1('Tom Jones', 50000)

    # same as Manager1.__getattribute__(tom, 'last_name')()
    print(tom.last_name())  # ** last_name
                            # ** person
                            # Jones
    print('')

    tom.give_raise(.10)  # ** person... same as Manager1.give_raise(tom, 0.10)

    # same as... Manager1.__repr__(tom)
    print(tom)  # ** person
                # [Person: Tom Jones, 60000]
    print('')

    tommy = Manager2('Tommy Jonesy', 50000)

    # same as Manager2.__getattribute__(tommy, 'last_name')()
    print(tommy.last_name())  # ** last_name
                              # ** person
                              # Jonsey
    print('')

    # same as Manager2.__getattribute__(tommy, 'give_raise')(0.10)
    tommy.give_raise(.10)  # ** give_raise
                           # ** person
    # printing not routed through generic __getattribute__() here
    print(tommy)  # <__main__.Manager2 object at 0x...>
    print('')

    # ** __repr__
    # ** person
    # [Person: Tommy Jonesy, 60000]
    print(Manager2.__getattribute__(tommy, '__repr__')())
    print('')
    
    thomas = Manager3('Thomas Jones', 50000)

    # same as Manager3.__getattribute__(thomas, 'last_name')()
    print(thomas.last_name())  # ** last_name
                               # Jones
    print('')

    # same as Manager3.__getattribute__(thomas, 'give_raise')(0.10)
    thomas.give_raise(.10)  # ** give_raise

    # calls redefined __repr__ method here... still not routed
    # same as Manager3.__repr__(thomas)
    print(thomas)  # [Person: Thomas Jones, 60000]
    print('')

    print()
    print(Manager3.__getattribute__(thomas, '__repr__')())  # ** __repr__
                                                # [Person: Thomas Jones, 60000]
    print('')

