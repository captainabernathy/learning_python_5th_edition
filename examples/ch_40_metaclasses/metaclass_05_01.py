# usage: python3 metaclass_05_01.py

print('code snippets from pages 1423-1424\n')

# NOTE: by redefining the type object's __call__() method, it's possible for a
# metaclass to catch the creation call at the end of a class statement...
#
# however, the redefinitions of BOTH __new__() and __call__() must be careful
# to call # back to their original defaults in type if mean to make a class in
# the end...
#
# additionally, __call__() must invoke type to kick off the other two


class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call:', classname, supers, classdict, sep='\n...')
        print('')
        return type.__call__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SuperMeta.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))
        print('')


print('making metaclass...')


# NOTE: SuperMeta's __call__() method is not invoked in the call to SuperMeta
# when making SubMeta, which goes to type instead

# In SuperMeta.init:
# ...SubMeta
# ...(<class 'type'>,)
# ...{'__module__': '__main__', '__qualname__': 'SubMeta',
# '__new__': <function SubMeta.__new__ at 0x...>,
# '__init__': <function SubMeta.__init__ at 0x...>}
# ...init class object: ['__module__', '__new__', '__init__', '__doc__']
class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new:', classname, supers, classdict, sep='\n...')
        print('')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SubMeta.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))
        print('')


class Eggs:
    pass


print('making class...')


# In SuperMeta.call:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
#
# In SubMeta.new:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
#
# In SubMeta.init:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
# ...init class object: ['__module__', 'data', 'meth', '__doc__']
class Spam(Eggs, metaclass=SubMeta):
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

