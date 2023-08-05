# usage: python3 customization_same_argument_constraints.py

# common superclass... takes two arguments
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# a Chef1 is an Employee... its constructor takes a single argument
# calls Employee's constructor (__init__()) directly
class Chef1(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)  # direct dispatch


# a Server1 is an Employee... its constructor takes a single argument
# calls Employee's constructor (__init__())
class Server1(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)


# TwoJobs1 is a Chef1 and a Server1... and both Chef1's and Server1's
# constructors call Employee's constructor directly
# Chef1's constructor (__init__()) is found first in the mro, so it is the
# one that's called
# direct call... ok
class TwoJobs1(Chef1, Server1):
    pass


# TwoJobs1 is a Chef1 and a Server1... both Chef1's and Server1's
# constructors call Employee's constructor directly... AND TwoJobs11's
# constructor calls Employee's constructor directly, so this is the call that
# has the final say
# ok, but class hierarchy uses two dispatch techniques when on would do
class TwoJobs11(Chef1, Server1):
    def __init__(self, name):
        Employee.__init__(self, name, 70000)


# a Chef2 is an Employee... its constructor calls super() to instantiate
# Employee
class Chef2(Employee):
    def __init__(self, name):
        super().__init__(name, 50000)  # dispatch by super()


# a Server2 is an Employee... its constructor calls super() to instantiate
# Employee
class Server2(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)


# will cause problems... calls to super() ^^^ have different arguments
# NOTE: Chef2 and Server2's constructors take two arguments and Employee's
# takes three. both calls to super() in Chef2 and Server2 pass on an additional
# argument under the assumption that the argument will be forwarded on to
# Employee... HOWEVER, this is not the case, and the the call to super() from
# Chef2 will call Server2's constructor with the wrong number of arguments
class TwoJobs2(Chef2, Server2):
    pass


# still problematic... for the same reason as above, except it invokes Chef2's
# constructor with the wrong number of arguments
class TwoJobs22(Chef2, Server2):
    def __init__(self, name):
        super().__init__(name, 70000)


if __name__ == '__main__':
    print('code snippets from pages 1096-1097\n')

    bob = Chef1('Bob')
    sue = Server1('Sue')
    print(bob.salary)  # 50000
    print(sue.salary)  # 40000
    print('')

    tom = TwoJobs1('Tom')
    print(tom.salary)  # 50000... follows mro
    # (<class '__main__.TwoJobs11'>, <class '__main__.Chef1'>,
    #  <class '__main__.Server1'>, <class '__main__.Employee'>,
    #  <class 'object'>)
    print(TwoJobs1.__mro__)
    print('')

    tom = TwoJobs11('Tom')
    print(tom.salary)  # 70000
    # (<class '__main__.TwoJobs11'>, <class '__main__.Chef1'>,
    #  <class '__main__.Server1'>, <class '__main__.Employee'>,
    #  <class 'object'>)
    print(TwoJobs11.__mro__)
    print('')

    bob = Chef2('bob')
    sue = Server2('Sue')

    # ok for either subclass in isolation
    print(bob.salary)  # 50000
    print(sue.salary)  # 40000
    print('')

    try:
        tom = TwoJobs2('Tom')
    except TypeError as ex:
        # Server2.__init__() takes 2 positional arguments but 3 were given
        print(ex)
    print('')

    # (<class '__main__.TwoJbs2'>, <class '__main__.Chef2'>,
    #  <class '__main__.Server2'>, <class '__main__.Employee'>,
    #  <class 'object'>)
    print(TwoJobs2.__mro__)
    print('')

    print(Chef2.__mro__)
    print('')

    try:
        tom = TwoJobs22('Tom')
    except TypeError as ex:
        # Chef2.__init__() takes 2 positional arguments but 3 were given
        print(ex)
