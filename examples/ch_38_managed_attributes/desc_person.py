class Name:  # use (object) in 2.X
    '''
    name descriptor docs
    '''
    # returns instance's _name attribute
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name

    # assigns value to instance's _name attribute
    def __set__(self, instance, value):
        print('change...')
        instance._name = value

    # deletes instance's _name attribute
    def __delete__(self, instance):
        print('remove...')
        del instance._name


class Person1:  # use (object) in 2.X
    # constructor builds a Person1 with its _name attribute initialized to name
    def __init__(self, name):
        self._name = name

    name = Name()  # assign descriptor instance to name attribute


class SuperPerson:
    # constructor builds a SuperPerson with its _name attribute initialized to
    # name
    def __init__(self, name):
        self._name = name

    name = Name()  # assigns descriptor instance to name attribute


class Person2(SuperPerson):  # Descriptors are inherited (class attributes)
    pass


if __name__ == '__main__':
    print('code snippets from pages 1272-1273\n')

    bob = Person1('Bob Smith')
    print(bob.name)  # fetch... Bob Smith... Name.__get__()
    print('')

    bob.name = 'Robert Smith'  # change... Name.__set__()
    print(bob.name)  # fetch... Robert Smith... Name.__get__()
    print('')

    del bob.name  # remove... Name.__delete__()

    print('')
    print('-' * 20)
    print('')

    sue = Person1('Sue Jones')
    print(sue.name)  # fetch... Sue Jones... Name.__get__()
    print('')

    print(Name.__doc__)  # name descriptor docs
    print('')

    bob = Person2('Bob Smith')
    print(bob.name)  # fetch Bob Smith... Name.__get__()
    print('')

    bob.name = 'Robert Smith'  # change... Name.__set__()
    print(bob.name)  # fetch Robert Smith... Name.__get__()
    print('')

    del bob.name  # remove... Name.__delete__()

    print('')
    print('-' * 20)
    print('')

    sue = Person2('Sue Jones')
    print(sue.name)  # Sue Jones... Name.__get__()
    print('')

    print(Name.__doc__)  # name descriptor docs
    print('')
