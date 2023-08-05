# usage: python3 attribute_access_getattr_and_setattr.py

class Empty:
    # NOTE: __getattr__() serves a hook for generic attribute requests
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)


class Accesscontrol:
    # NOTE: __setattr__() serves as a hook for generic attribute assignments...
    # self.attr = value => self.__setattr__('attr',value)
    def __setattr__(self, attr, value):
        if attr == 'age':
            # not the same as self.name = x...
            # bc not assigning to the __dict__ itself...
            # also not the same as setattr
            self.__dict__[attr] = value + 10
            # object.__setattr__(self, attr, value + 10)  # ok
            # self.age = value + 10  # loops infinitely.. calling __setattr__()
            # setattr(self, attr, value + 10)  # loops infinitely
            # self.other = 99  # recurs but doesn't loop... just fails
        else:
            raise AttributeError(attr + ' not allowed')


if __name__ == '__main__':
    print('code snippets from pages 938-940\n')

    X = Empty()
    print(X.age)  # 40

    try:
        print(X.name)
    except AttributeError:
        print('AttributeError')
    print('')

    X = Empty()
    print(X.__getattr__('age'))  # 40
    print('')

    X = Accesscontrol()
    X.age = 40
    print(X.age)  # 50

    try:
        X.name = 'Bob'
    except AttributeError as ex:
        print(ex)
    print('')

    X = Accesscontrol()
    X.__setattr__('age', 40)
    print(X.age)  # 50
