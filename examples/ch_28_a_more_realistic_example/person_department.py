# usage: python3 person_department.py

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


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


class Department:
    # aggregates (positional) args into a list of members
    def __init__(self, *args):
        self.members = list(args)

    # appends person to this Department's members
    def add_member(self, person):
        self.members.append(person)

    # gives each person in this Department a raise
    def give_raises(self, percent):
        for person in self.members:
            person.give_raise(percent)

    # displays each person in this Department's members
    def show_all(self):
        for person in self.members:
            print(person)  # invokes Person's __repr__()


if __name__ == '__main__':
    print('code snippets from pages 866-867\n')

    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)

    # build a Department with bob and sue
    development = Department(bob, sue)

    # add tom to the development Department
    development.add_member(tom)

    # give everyone in the development Department a raise
    development.give_raises(.10)

    # display everyone in the development Department
    # [Person: Bob Smith, 0]
    # [Person: Sue Jones, 110000]
    # [Person: Tom Jones, 60000]
    development.show_all()
