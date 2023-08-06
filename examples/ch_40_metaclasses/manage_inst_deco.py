# usage: python3 manage_inst_deco.py

# can be used as a class decorator to trace extended instance attribute
# accesses
def Tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kargs):
            self.wrapped = aClass(*args, **kargs)

        def __getattr__(self, attrname):  # catches all but .wrapped
            print('Trace:', attrname)
            return getattr(self.wrapped, attrname)  # delegate to wrapped obj
    return Wrapper  # return handle to Wrapper


@Tracer
class Person:  # Person = Tracer(Person)
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


if __name__ == '__main__':
    print('code snippets from page 1443\n')

    bob = Person('Bob', 40, 50)

    print(bob.name)  # Trace: name... bob
    print('')

    print(bob.pay())  # Trace: pay... 2000
    print('')
