# NOTE: delegation-based classes must redefine some operator overloading
# methods (ie: __repr__, __str__) to route them to embedded objects in 3.X, but
# NOT in 2.X (unless new-style classes are used)

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


class Manager1:
    # constructor builds a Manager1 with its person attribute initialized
    # to name, 'mgr', and pay
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)  # embedded person object

    # updates this Manager1's person attribute's pay by percent + bonus
    def give_raise(self, percent, bonus=0.10):
        self.person.give_raise(percent + bonus)  # intercept and delegate

    # returns lookups for this Manager1's attr through it's person attribute
    # (ie: obj.attr => obj.person.attr)
    def __getattr__(self, attr):
        return getattr(self.person, attr)  # delegate all other sttrs

    # returns the string representation of this Manager1 through the string
    # representation of its person attribute
    def __repr__(self):
        return str(self.person)  # overload here required in 3.X
    

# same as Manager1 except without a __repr__() method
class Manager2:
    # constructor builds a Manager2 with its person attribute initialized
    # to name, 'mgr', and pay
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)  # embedded person object

    # updates this Manager2's person attribute's pay by percent + bonus
    def give_raise(self, percent, bonus=0.10):
        self.person.give_raise(percent + bonus)  # intercept and delegate

    # returns lookups for this Manager2's attr through it's person attribute
    # (ie: obj.attr => obj.person.attr)
    def __getattr__(self, attr):
        return getattr(self.person, attr)  # delegate all other sttrs


if __name__ == '__main__':
    print('code snippets from pages 1296-1297\n')

    sue = Person('Sue Jones', job='dev', pay=100000)
    print(sue.last_name())  # Jones... same as Person.last_name(sue)
    print('')

    sue.give_raise(.10)  # same as Person.give_raise(sue, 0.10)
    print(sue)  # [Person: Sue Jones, 110000]... same as Person.__repr__(sue)
    print('')

    tom = Manager1('Tom Jones', 50000)
    
    print(tom.last_name())  # Jones...
                            # same as Manager1.__getattr__(tom, 'last_name')()
    print('')

    tom.give_raise(.10)  # same as Manager1.give_raise(tom, 0.10)
    
    print(tom)  # [Person: Tom Jones, 60000]... same as Manager1.__repr__(tom)
    print('')

    tommy = Manager2('Tommy Jonesy', 50000)

    print(tommy.last_name())  # Jonsey...
                        # same as Manager2.__getattr__(tommy, 'last_name')()
    print('')

    tommy.give_raise(.10)  # same as Manager2.give_raise(tommy, 0.10)

    # printing not routed through generic __getattr__() in 3X here
    print(tommy)  # <__main__.Manager2 object at 0x...>... in 3X
                  # [Person: Tommy Jonesy, 60000]... in 2X

    # HOWEVER, explict call outputs... [Person: Tommy Jonesy, 60000]
    print(Manager2.__getattr__(tommy, '__repr__')())
    print('')
