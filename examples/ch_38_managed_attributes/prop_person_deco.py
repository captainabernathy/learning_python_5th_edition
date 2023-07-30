class Person:
    # constructor builds a Person object with it's _name attribute initialized
    # to name
    def __init__(self, name):
        self._name = name

    # NOTE: in Python >= 2.6 and 3.0, property objects have getter, setter, and
    # deleter methods that can be associated with the corresponding methods
    
    # NOTE: the getter component is usually filled in automatically by the
    # act of creating a property

    # here, the property buit-in serves as a decoator to define a function that
    # will run automatically when this Person's name attribue is accessed
    @property
    def name(self):  # rebinds: name = property(name)
        '''
        name property docs
        '''
        print('fetch...')
        return self._name

    # delegates a setter method associated with the property name... that sets
    # this Person's _name attribute to name
    @name.setter
    def name(self, value):  # name = name.setter(name)
        print('change...')
        self._name = value

    # delegates a deleter method associated with the property name... that
    # deletes this Person's _name attribute
    @name.deleter
    def name(self):  # name = name.deleter(name)
        print('remove...')
        del self._name


if __name__ == '__main__':
    print('code snippets from pages 1267-1268\n')

    bob = Person('Bob Smith')
    print(bob.name)  # fetch... Bob Smith... runs getter
    print('')

    bob.name = 'Robert Smith'  # change... runs name.setter
    print(bob.name)  # fetch... Robert Smith...  runs getter
    print('')

    del bob.name  # remove... runs name.deleter

    print('')
    print('-' * 20)
    print('')

    sue = Person('Sue Jones')
    print(sue.name)  # fetch... Sue Jones... runs getter
    print('')

    print(Person.name.__doc__)  # name property docs
    print('')
