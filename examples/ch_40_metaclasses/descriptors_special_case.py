# usage: python3 descriptors_special_case.py

class C1:
    pass


# descriptor class that provides both __get__() and __set__() methods
class D2:
    def __get__(self, instance, owner):
        print('__get__')

    def __set__(self, instance, owner):
        print('__set__')


# C2 has an attribute that is an instance of D2
class C2:
    d = D2()


# descriptor class that provides only a __get__() method
class D3:
    def __get__(self, instance, owner):
        print('__get__')


# C3 has an attribute that is an instance of D3
class C3:
    d = D3()


if __name__ == '__main__':
    print('code snippets from pages 1431-1432\n')

    I1 = C1()

    print(I1.__class__)  # <class '__main__.C1'>
    print(I1.__dict__)  # {}
    print('')

    I1.__dict__['name'] = 'bob'
    I1.__dict__['class'] = 'spam'
    I1.__dict__['__dict__'] = {}

    print(I1.name)  # bob
    print(I1.__class__)  # <class '__main__.C1'>
    print(I1.__dict__)  # {'name':'bob','class':'spam','__dict__':{}}
    print('')

    I2 = C2()

    I2.d  # __get__
    I2.d = 1  # __set__
    print('')

    I2.__dict__['d'] = 'spam'  # define same name in instance namespace dict
    I2.d  # __get__... ^^^ doesn't hide data descriptor in class
    print('')

    I3 = C3()

    I3.d  # __get__
    print('')

    I3.__dict__['d'] = 'spam'  # hides class attributes of the same name per
                               # inheritance rules
    print(I3.d)  # spam
    
