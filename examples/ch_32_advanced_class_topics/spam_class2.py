class Spam:
    num_instances = 0  # counts the number of Spam instances... starts at zero

    # constructor... passes self.__class__ to count()
    def __init__(self):
        self.count()

    # increments per-class instance counter
    def count(cls):
        cls.num_instances += 1  # cls is is the lowest class above instance

    # ensures that calls to count() from Spam and Spam instances implicitly
    # pass a reference to Spam
    count = classmethod(count)


# inherits class methods
class Sub(Spam):
    # overrides Spam's num_instances
    num_instances = 0

    # overrides Spam's constructor
    def __init__(self):
        # calls Spam's constructor passing it a reference to this Sub
        Spam.__init__(self)


# inherits class methods
class Other(Spam):
    # overrides Spam's num_instances
    num_instances = 0
