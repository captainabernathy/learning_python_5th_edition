# usage: python3 desc_person_nested.py

class Person:
    # constructor builds a Person with its _name attribute initialized to name
    def __init__(self, name):
        self._name = name

    # NOTE: here, Name is local to the scope of the Person class
    class Name:  # nested class
        '''
        name descriptor docs
        '''
        # returns instance's _name attribute
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name

        # sets instance's _name attribute to value
        def __set__(self, instance, value):
            print('change...')
            instance._name = value

        # deletes instance's _name attribute
        def __delete__(self, instance):
            print('remove...')
            del instance._name

    name = Name()  # assigns descriptor instance to name attribute


if __name__ == '__main__':
    print('code snippets from page 1273\n')

    bob = Person('Bob Smith')
    print(bob.name)  # fetch... Bob Smith... Person.Name.__get__()
    print('')

    bob.name = 'Robert Smith'  # change... Name.__set__()
    print(bob.name)  # fetch... Robert Smith... Person.Name.__get__()
    print('')

    del bob.name

    print('')
    print('-' * 20)
    print('')

    sue = Person('Sue Jones')  # inherits descriptors
    print(sue.name)  # fetch.. Sue Jones... Person.Name.__get__()
    print(Person.Name.__doc__)  # name descriptor docs
