# usage: python3 metaclass_04_super.py

print('code snippets from page 1422\n')


# a super class that mimics the dispatch of type in terms of metaclass dispatch
class SuperMetaObj:
    def __call__(self, classname, supers, classdict):
        print('In SuperMetaObj.call:', classname, supers, classdict,
              sep='\n...')
        print('')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class


# initialization of super class enables this clas to acquire the __call__()
# interceptor, which facilitates the use of this class a a metaclass
class SubMetaObj(SuperMetaObj):
    def __New__(self, classname, supers, classdict):
        print('In SubMetaObj.New:', classname, supers, classdict, sep='\n...')
        print('')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In SubMetaObj.Init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))
        print('')


class Eggs:
    pass


print('making class...')


# In SuperMetaObj.call:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
#
# In SubMetaObj.New:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
#
# In SubMetaObj.Init:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
# ...init class object: ['__module__', 'data', 'meth', '__doc__']
class Spam(Eggs, metaclass=SubMetaObj()):
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
