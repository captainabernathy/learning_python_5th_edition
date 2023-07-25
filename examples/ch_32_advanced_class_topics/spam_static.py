class Spam:
    num_instances = 0  # counts the number of Spam instances... starts at zero

    # constructor... increments the number of Spam instances whenever a new
    # Spam object is created
    def __init__(self):
        Spam.num_instances += 1

    # outputs the number of instances of Spam objects
    def print_num_instances():
        print('Number of instances %s' % Spam.num_instances)

    # makes print_num_instances() callable through Spam or an instance of it
    print_num_instances = staticmethod(print_num_instances)


class Sub(Spam):

    # overrides Spam's print_num_instances()
    def print_num_instances():
        print('Extra stuff...')
        # calls back to Spam's print_num_instances() before returning
        Spam.print_num_instances()

    # makes print_num_instances() callable through Sub or an instance of it
    print_num_instances = staticmethod(print_num_instances)


# NOTE: static methods defined in one class are inherited by its children
class Other(Spam):
    pass  # inherits static methods
