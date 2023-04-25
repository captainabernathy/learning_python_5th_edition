from __future__ import print_function  # for 2.X/3.X interoperability


class Employee:
    # constructor intializes this Employee's name and salary attributes
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    # increases this Employee's salary by a specified percent
    def give_raise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    # outputs what his employee is doing
    def work(self):
        print(self.name, 'does stuff')

    # returns a string representation of this Employee
    def __repr__(self):
        return '<Employee: name=%s, salary=%s>' % (self.name, self.salary)


# a Chef is an Employee
class Chef(Employee):

    # constructor initializes this Chef with a name attribute as specified
    # and a salary of 50000
    def __init__(self, name):
        Employee.__init__(self, name, 50000)  # calls parent's constructor

    # overrides Employee's work() method
    def work(self):
        print(self.name, 'makes food')


# a Server is an Employee
class Server(Employee):
    # constructor initializes this Server with a name attribute as specified
    # and a salary of 40000
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    # overrides Employee's work() method
    def work(self):
        print(self.name, 'interfaces with customer')


# a PizzaRobot is a Chef
class PizzaRobot(Chef):
    # constructor initializes this PizzaRobot with a name attribute as
    # specified
    def __init__(self, name):
        Chef.__init__(self, name)

    # overrides Chef's work() method
    def work(self):
        print(self.name, 'makes pizza')


if __name__ == '__main__':
    print('code snippets from pages 965-966\n')

    bob = PizzaRobot('bob')
    # <Employee: name=bob, salary=50000.0>
    print(bob)  # calls  __repr__() inherited from Employee
    bob.work()  # bob makes pizza
    bob.give_raise(0.20)  # calls give_raise() inherited from Employee
    print(bob)  # <Employee: name=bob, salary=60000.0>
    print('')

    # loop over each class type
    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)  # create an instance of each class type
        obj.work()  # call each instance's work() method
