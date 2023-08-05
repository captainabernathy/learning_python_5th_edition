# usage: python3 classes_are_objects_generic_object_factories.py

# returns an instance of aClass constructed with any number of positional and
# keyword arguments
def factory(aClass, *pargs, **kargs):  # varargs tuple, dict
    return aClass(*pargs, **kargs)


class Spam:
    def doit(self, message):  # bound method
        print(message)


class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job


if __name__ == '__main__':
    print('code snippets from page 986\n')

    obj1 = factory(Spam)
    obj2 = factory(Person, 'Arthur', 'King')
    obj3 = factory(Person, name='Brian')
    obj1.doit(99)  # 99
    print(obj2.name, obj2.job)  # Arthur King
    print(obj3.name, obj3.job)  # Brian None
