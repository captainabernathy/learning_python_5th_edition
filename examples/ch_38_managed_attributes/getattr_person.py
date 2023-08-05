# usage: python3 getattr_person.py

class Person:
    # constructor builds a Person with its _name attribute initialized to name
    def __init__(self, name):  # portable in 2.X or 3.X
        self._name = name  # triggers __setattr__() on Person() calls

    # returns this Person's _name attribute on accesses to this Person's
    # name attribute (ie: obj.name)... raises an AttributeError otherwise
    def __getattr__(self, attr):
        '''
        called on obj.undefined
        '''
        print('get: ' + attr)
        if attr == 'name':     # intercept name
            return self._name  # does not loop
        else:
            raise AttributeError(attr)

    # sets this Person's _name attribute to value on assignments to this
    # Person's name attribute (ie: obj.name = value)
    def __setattr__(self, attr, value):
        '''
        called on obj.any = value
        '''
        print('set: ' + attr)
        if attr == 'name':  # set internal name
            attr = '_name'
        self.__dict__[attr] = value  # avoid looping

    # deletes this Person's _name attribute on del opertions to this Person's
    # name attribute (ie: del obj.name)
    def __delattr__(self, attr):
        '''
        called on del obj.any
        '''
        print('del: ' + attr)
        if attr == 'name':
            attr = '_name'
        del self.__dict__[attr]  # avoid looping


if __name__ == '__main__':
    print('code snippets from page 1284\n')

    bob = Person('Bob Smith')  # set: _name
    print('')

    print(bob.name)  # get: name... Bob Smith...
                     # same as Person.__getattr__(bob, 'name')
    print('')

    bob.name = 'Robert Smith'  # set: name... same as
                            # Person.__setattr__(bob, 'name', 'Robert Smith')
    print('')

    print(bob.name)  # get: name... Rober Smith
                     # same as Person.__getattr__(bob, 'name')
    print('')

    del bob.name  # del: name... same as Person.__delattr__(bob, 'name')
    
    print('')
    print('-' * 20)
    print('')
    
    sue = Person('Sue Jones')  # set: _name
    print('')
    print(sue.name)  # get: name... Sue Jones...
                     # same as Person.__getattr__(sue, 'name')
    print('')
