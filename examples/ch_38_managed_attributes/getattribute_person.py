# usage: python3 getattribute_person.py

class Person:
    # constructor builds a Person with its _name attribute initialized to name
    def __init__(self, name):  # portable on 2.X or 3.X
        self._name = name

    # returns this Person's _name attribute on accesses to this Person's name
    # attribute (ie: obj.name)
    def __getattribute__(self, attr):
        '''
        called on obj.any
        '''
        print('get: ' + attr)
        if attr == 'name':  # map to internal name
            attr = '_name'
        # NOTE: since __getattribute__() runs for all attribute accesses, an
        # attempt to return self._name would result in infinite recursion
        return object.__getattribute__(self, attr)  # avoid loop

    # sets this Person's _name attribute to value on assignments to this
    # Person's name attribute (ie: obj.name = value)
    def __setattr__(self, attr, value):
        '''
        called on obj.any = value
        '''
        print('set: ' + attr)
        if attr == 'name':  # set internal name
            attr = '_name'

        # NOTE self.__dict__ invokes __getattribute__(self, '__dict__')

        # below same as Person.__getattribute__(self, '__dict__')[attr] = value
        self.__dict__[attr] = value  # avoid looping

    # deletes this Person's _name attribute on del operations to this Person's
    # name attribute (ie: del obj.name)
    def __delattr__(self, attr):
        '''
        called on del obj.any
        '''
        print('del: ' + attr)
        if attr == 'name':
            attr = '_name'

        # below same as del Person.__getattribute__(self, '__dict__')[attr]
        del self.__dict__[attr]  # avoid looping


if __name__ == '__main__':
    print('code snippets from page 1285\n')

    bob = Person('Bob Smith')  # set: _name... get: __dict__
    print('')

    print(bob.name)  # get: name... Bob Smith...
                     # same as Person.__getattribute__(bob, 'name')
    print('')

    bob.name = 'Robert Smith'  # set: name... get: __dict__
                    # same as Person.__setattr__(bob, 'name', 'Robert Smith')
    print('')
    print(bob.name)  # get: name... Robert Smith
                     # same as Person.__getattribute__(bob, 'name')
    print('')

    del bob.name  # del: name... get: __dict__
                  # same as Person.__delattr__(bob, 'name')

    print('')
    print('-' * 20)
    sue = Person('Sue Jones')  # set: _name... get: __dict__
    print('')

    print(sue.name)  # get: name... Sue Jones
                     # same as Person.__getattribute__(sue, 'name')
    print('')
