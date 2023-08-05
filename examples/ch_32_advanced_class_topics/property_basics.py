# usage: python(2/3) property_basics.py

from __future__ import print_function


class operators:
    # called on undefined reference
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

    # called on assignments or object.__setattr__()
    def __setattr__(self, name, value):
        print('set: %s %s' % (name, value))
        if name == 'age':
            self.__dict__['_age'] = value
        else:
            self.__dict__[name] = value


class properties(object):  # object needed for 2.X
    def getage(self):
        return 40

    def setage(self, value):
        print('set age: %s' % value)
        self._age = value

    # NOTE: use the built-in property() function to generate a property in
    # a class... property() takes four attributes where each is a handle to a
    # function that corresponds to the operations get, set, delete, and
    # docstring, respectively
    age = property(getage, setage, None, None)


if __name__ == '__main__':
    print('code snippets from pages 1056-1058\n')

    X = operators()
    print(X.age)  # calls __getattr__()
    print('')

    X.age = 41  # calls __setattr__()... sets X._age

    print(X._age)  # 41... calls __getattr__
    print('')

    print(X.age)  # 40... calls __getattr__()
    print('')

    X.job = 'trainer'  # calls __setattr__()... sets X.job
    print(X.job)  # trainer... calls __getattr__()
    print('')

    X = properties()
    print(X.age)  # 40... calls getage()
    print('')

    X.age = 42  # calls setage()... sets X._age
    
    print(X._age)  # 42... normal access, doesn't call getage()
    print('')

    print(X.age)  # calls getage()
    print('')

    X.job = 'trainer'  # normal assignment... no job proerty

    print(X.job)  # trainer... normal access... no job property

