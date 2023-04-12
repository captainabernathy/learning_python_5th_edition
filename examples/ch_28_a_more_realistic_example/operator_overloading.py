class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # NOTE: __repr__() acts a fallback/alternative for __str__()... it returns
    # a string that is output when an object is printed
    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob)  # [Person: Bob Smith, 0]
    print(sue)  # [Person: Sue Jones, 100000]
    print(bob.last_name(), sue.last_name())  # Smith Jones

    sue.give_raise(0.10)
    print(sue)  # [Person: Sue Jones, 110000]
