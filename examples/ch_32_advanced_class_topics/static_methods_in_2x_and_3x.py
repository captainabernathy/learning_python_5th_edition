# usage: python(2/3) static_methods_in_2x_and_3x.py

# NOTE: in 3X it is not necessary to declare a method as static in order to
# call it from the class, BUT it IS necessary to declare the method as static
# in order to call it from an instance
#
# in 2X it is always necessary to declare a method as static in order to be
# able to call it from the class or an instance
from __future__ import print_function


class Spam:
    num_instances = 0  # counts the number of Spam instances... starts at zero

    # constructor... increments the number of Spam instances whenever a new
    # Spam object is created
    def __init__(self):
        Spam.num_instances += 1

    # unbound method... function callable only from the class in 3X
    def print_num_instances():
        print('Number of instances created: %s' % Spam.num_instances)


if __name__ == '__main__':
    print('code snippets from pages 1061-1062\n')

    a = Spam()
    b = Spam()
    c = Spam()

    try:
        # fails in 2X, but works in 3X
        Spam.print_num_instances()  # Number of instances created: 3... in 3X
    except TypeError as ex:
        print(ex)  # unbound method print_num_instances() must be called with
                   # Spam instance as first argument... in 2X
    print('')

    try:
        a.print_num_instances()  # fails in 2X and 3X unless declared static
    except TypeError as ex:
        print(ex)  # print_num_instances() takes no arguments (1 given)
