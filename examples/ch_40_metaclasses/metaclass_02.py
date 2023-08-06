# python3 metaclass_02.py

print('code snippets from page 1419\n')


# NOTE: metaclasses can use either __new__() or __init__() or both to manage a
# class at creation time
#
# while __new__() creates and returns a class object, __init__()
# initializes the already created class passed in as an argument
class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new:', classname, supers, classdict,
              sep='\n...')
        print('')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaTwo.init:', classname, supers, classdict,
              sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))
        print('')


class Eggs:
    pass


print('making class...')


# as soon as the class statement is processed...
# In MetaTwo.new:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
#
# In MetaTwo.init:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
# ...init class object: ['__module__', 'data', 'meth', '__doc__']
class Spam(Eggs, metaclass=MetaTwo):
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

