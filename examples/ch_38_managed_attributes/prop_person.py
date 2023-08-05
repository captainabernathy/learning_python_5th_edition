# usage: python3 prop_person.py

class Person1:
    # constructor builds a Person1 object with it's _name attribute initialized
    # to name
    def __init__(self, name):
        self._name = name

    # returns this Person1's _name attribute
    def get_name(self):
        print('fetch...')
        return self._name

    # sets this Person1's _name attribute to value
    def set_name(self, value):
        print('change...')
        self._name = value

    # deletes this Person1's _name attribute
    def del_name(self):
        print('remove...')
        del self._name

    # NOTE: property() returns a property object that is assigned to the name
    # of an attribute to be managed in class scope... here, 'name' is the
    # named attribute, and its access, assignment, and removal operations will
    # be handled by the provided methods
    name = property(get_name, set_name, del_name, 'name property docs')


class SuperPerson:
    # constructor builds a SuperPerson object with it's _name attribute
    # initialized to name
    def __init__(self, name):
        self._name = name

    # returns this SuperPerson's _name attribute
    def get_name(self):
        print('fetch...')
        return self._name

    # sets this SuperPerson's _name attribute to value
    def set_name(self, value):
        print('change...')
        self._name = value

    # deletes this SuperPerson's _name attribute
    def del_name(self):
        print('remove...')
        del self._name

    # NOTE: properties are inherited by subclasses
    name = property(get_name, set_name, del_name, 'name property docs')


class Person2(SuperPerson):
    pass  # inherits properties


if __name__ == '__main__':
    print('code snippets from pages 1264-1265\n')

    bob = Person1('Bob Smith')  # bob has a managed name attribute
    print(bob.name)  # fetch... Bob Smith...  same as Person1.get_name(bob)
    print('')

    bob.name = 'Robert Smith'  # change...
                               # same as Person1.set_name(bob, 'Robert Smith')

    print(bob.name)  # fetch... Robert Smith... same as Person1.get_name(bob)
    print('')

    del bob.name  # remove... same as Person1.del_name(bob)

    print('')
    print('-' * 20)
    print('')

    sue = Person1('Sue Jones')  # sue has a managed name attribute
    print(sue.name)  # fetch... Sue Jones... same as Person1.get_name(sue)
    print('')

    print(Person1.name.__doc__)  # name property docs
    print('')

    bob = Person2('Bob Smith')  # bob has a managed name attribute

    print(bob.name)  # fetch... Bob Smith... same as Person2.get_name(bob)
    print('')

    bob.name = 'Robert Smith'  # chagne...
                               # same as Person2.set_name(bob, 'Robert Smith')
    print(bob.name)  # fetch... Bob Smith... same as Person2.get_name(bob)
    print('')

    del bob.name  # remove... same as Person2.del_name(bob)

    print('')
    print('-' * 20)
    print('')

    sue = Person2('Sue Jones')  # sue inherits a managed name attribute
    print(sue.name)  # fetch... Sue Jones... same as Person2.get_name(sue)
    print('')

    print(Person2.name.__doc__)  # name property docs
    print('')
