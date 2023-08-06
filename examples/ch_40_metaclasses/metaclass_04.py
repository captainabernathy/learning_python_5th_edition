# usage: python3 metaclass_04.py

print('code snippets from page 1421\n')


# class that provides a __call__() method for its instances that catches a
# metaclass call using the operator
class MetaObj:
    def __call__(self, classname, supers, classdict):
        print('In MetaObj.call:', classname, supers, classdict, sep='\n...')
        print('')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class

    # NOTE: it is necessary for __new__() and __init__() to have different
    # names so that they DO NOT run when the instance is created... as opposed
    # to the time they are supposed to run in the role of the metaclass
    def __New__(self, classname, supers, classdict):
        print('In MetaObj.New:', classname, supers, classdict, sep='\n...')
        print('')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In MetaObj.Init:', classname, supers, classdict, sep='\n...')
        print('...Init class object:', list(Class.__dict__.keys()))
        print('')


class Eggs:
    pass


print('making class...')


# In MetaObj.call:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
#
# In MetaObj.New:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
#
# In MetaObj.Init:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
# ...Init class object: ['__module__', 'data', 'meth', '__doc__']
class Spam(Eggs, metaclass=MetaObj()):
    data = 1

    def meth(self, arg):
        return self.data + arg


if __name__ == '__main__':
    print('making instance...\n')

    X = Spam()

    print(X.data)  # 1
    print('')

    print(X.meth(2))  # 3
    print('')

