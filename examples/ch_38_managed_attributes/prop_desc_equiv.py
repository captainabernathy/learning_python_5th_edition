# usage: pyton3 prop_desc_equiv.py

class Property:
    '''
    Descriptor that simulates the property built-in
    '''

    # constructor builds a Property with its fget, fset, fdel, and doc
    # attributes initialized as provided
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    # the result of calling this Property's fget method on instance if it is
    # defined... otherwise retuns this Property if instance is not defined or
    # raises an AttributeError if this instance's fget method is not defined
    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self

        if self.fget is None:
            raise AttributeError('can\'t get attribute')

        # Pass instance to self in property accessors
        return self.fget(instance)

    # calls this Property's fset method on instance and value if the method is
    # defined... otherwise raises an AttributeError
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('can\'t set attribute')
        self.fset(instance, value)

    # calls this Property's fdel method on instance if the method is defined...
    # otherwise raises an AttributeError
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError('can\'t delete attribute')
        self.fdel(instance)


class Person:
    def get_name(self):
        print('get_name...')

    def set_name(self, value):
        print('set_name...')

    # assigns a Property object initialized with get_name and set_name to the
    # attribute name
    name = Property(get_name, set_name)


if __name__ == '__main__':
    print('code snippet from page 1278\n')

    x = Person()
    x.name  # get_name...
    print('')

    x.name = 'Bob'  # set_name...
    print('')

    try:
        del x.name  # error!
    except AttributeError as ex:
        print(ex)  # can't delete attribute
    print('')
