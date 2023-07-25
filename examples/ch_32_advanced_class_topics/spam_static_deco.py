# NOTE: the @ symbol introduces a metafunction or other callable object
# than manages another function or callable object
# @ rebinds a method's name to a decoration... effectively...
#   @staticmethod
#   def f():
#       ...
# is equivalent to:
#   def f()
#       ...
#   f = staticmethod(f)

class Spam:
    # counts the number of Spam instances
    num_instances = 0

    # constructor... increments the number of Spam instances
    def __init__(self):
        Spam.num_instances += 1

    # NOTE: static methods have no self argument, are designed to work with
    # class attributes, and can be called through the class or an instance
    @staticmethod
    def print_num_instances():
        print('Number of instances created: %s' % Spam.num_instances)
