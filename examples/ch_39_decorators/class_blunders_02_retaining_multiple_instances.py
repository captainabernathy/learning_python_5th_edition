# handles multiple classes but won't work for multiple instances of a given
# class... each instance construction triggers __call__(), which overwirtes the
# prior instance... so it only saves the last one created

# NOTE: the problem is that we make one decorator instance per class, but not
# per class instance
class Tracer:
    def __init__(self, acls):
        self.acls = acls

    def __call__(self, *args):
        self.wrapped = self.acls(*args)
        return self

    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)


@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)


@Tracer
class Person:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    print('code snippets from pages 1353-1354\n')

    food = Spam()  # Triggers __call__()
    food.display()  # Trace: display.. Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!
                    # Triggers __getattr__()
    print('')

    bob = Person('bob')  # Trace: name... bob
    print(bob.name)
    print('')

    Sue = Person('Sue')  # Sue overwrites bob

    print(Sue.name)  # Trace: name... Sue
    print('')

    print(bob.name)  # Trace: name... Sue
    print('')
