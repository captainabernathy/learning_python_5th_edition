# usage: python3 manage_inst_meta.py

# NOTE: to use a metaclass to manage instances, it is necessasry to take on
# the additional responsibility for creating the class as well

# can be used as a metaclass to manage class instances... uses the metaclass
# protocol to imitate decorators
def Tracer(classname, supers, classdict):
    # manually create subject class
    aClass = type(classname, supers, classdict)

    class Wrapper:
        def __init__(self, *args, **kargs):
            self.wrapped = aClass(*args, **kargs)

        def __getattr__(self, attrname):
            print('Trace:', attrname)
            return getattr(self.wrapped, attrname)
    return Wrapper  # return instance Wrapper


class Person(metaclass=Tracer):
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


if __name__ == '__main__':
    print('code snippets from pages 1443-1444\n')

    bob = Person('Bob', 40, 50)

    print(bob.name)  # Trace: name... Bob
    print('')

    print(bob.pay())  # Trace: pay... 2000
    print('')

