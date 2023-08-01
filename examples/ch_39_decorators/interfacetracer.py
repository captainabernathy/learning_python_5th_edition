# Original nondecorator delegation example
class Wrapper:
    '''
    intercepts access to any of the wrapped object's named attributes, prints
    a trace message, and uses the getattr built-in to pass off the request to
    the wrapped object
    '''
    def __init__(self, object):
        self.wrapped = object  # save object

    def __getattr__(self, attrname):
        print('Trace:', attrname)  # Trace fetch
        return getattr(self.wrapped, attrname)  # Delegate fetch


def Tracer(acls):  # runs on @Tracer decoration
    
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = acls(*args, **kwargs)  # use enclosing scope name

        def __getattr__(self, attrname):
            print('Trace:', attrname)  # catches all but own attrs
            self.fetches += 1
            return getattr(self.wrapped, attrname)

    return Wrapper


@Tracer
class Spam:
    # Spam = Tracer(Spam)
    # Spam is rebound to Wrapper
    def display(self):
        print('Spam!' * 8)


@Tracer
class Person:
    # Person = Tracer(Person)
    # Wrapper remembers Person
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        # Accesses outside of class traced
        # In-method accesses not traced
        return self.hours * self.rate


if __name__ == '__main__':
    print('code snippets from pages 1349-1351\n')

    x = Wrapper([1, 2, 3])  # wrap a list
    x.append(4)  # Trace: append... delegate to list method
    print(x.wrapped)  # [1,2,3,4]
    print('')

    x = Wrapper({'a': 1, 'b': 2})  # wrap a dictionary
    print(list(x.keys()))  # Trace: keys.. ['a','b'].. delegate to dict method
    print('')

    food = Spam()  # Triggers Wrapper()
    food.display()  # Trace: display...
                    # Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!...
                    # Triggers __getattr__
    print('')

    print([food.fetches])  # [1]
    print('')

    bob = Person('Bob', 40, 50)  # bob is really a Wrapper
    print(bob.name)  # Trace: name... Bob... Wrapper embeds a Person
    print('')

    print(bob.pay())  # Trace: pay... 2000
    print('')

    sue = Person('Sue', rate=100, hours=60)  # sue is a different wrapper
    print(sue.name)  # Trace: name... Sue... with a different Person
    print('')

    print(sue.pay())  # Trace: pay... 6000
    print('')

    print(bob.name)  # Trace: name... Bob... Wrapper embeds a Person
    print('')

    print(bob.pay())  # Trace: pay... 2000
    print('')

    print([bob.fetches, sue.fetches])  # [4, 2]... Wrapper attrs not traced
    print('')
