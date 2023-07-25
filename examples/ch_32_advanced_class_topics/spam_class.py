class Spam:
    num_instances = 0  # counts the number of Spam instances... starts at zero

    # constructor... increments the number of Spam instances whenever a new
    # Spam object is created
    def __init__(self):
        Spam.num_instances += 1

    # prints the number of instances of Spam classes
    def print_num_instances(cls):
        print('Number of instances: %s %s' % (cls.num_instances, cls))

    # ensures that calls to print_num_instances() from Spam and Spam instances
    # implicitly pass a reference to Spam
    print_num_instances = classmethod(print_num_instances)


class Sub(Spam):
    # overrides Spam's print_num_instances()
    def print_num_instances(cls):
        print('Extra stuff...', cls)
        # calls back to Spam's print_num_instances()
        Spam.print_num_instances()

    # ensures that calls to print_num_instances() from Sub and Sub instances
    # implicitly pass a reference to Sub
    print_num_instances = classmethod(print_num_instances)


class Other(Spam):
    pass  # inherits class methods
