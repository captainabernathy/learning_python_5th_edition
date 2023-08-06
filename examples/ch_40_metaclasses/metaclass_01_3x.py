# usage: python3 metaclass_01_3x.py

print('code snippets from pages 1417-1418\n')


class MetaOne(type):
    # NOTE: a metaclass __new__() is run by (the inherited) type's
    # __call__() method, performs customizations, an calls type's __new__
    # method to create and return the new class object
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict,
              sep='\n...')
        print('')
        return type.__new__(meta, classname, supers, classdict)


class Eggs:
    pass


print('making class...')


# as soon as the class statement is processed...
# In MetaOne.new:
# ...<class '__main__.MetaOne'>
# ...Spam
# ...(<class '__main__.Eggs'>)
# ...{'__module__':'__main__','__qualname__':'Spam','data':1,
# 'meth':<function Spam.meth at 0x...>}

# NOTE: Spam inherits from eggs and is an instance of MetaOne
class Spam(Eggs, metaclass=MetaOne):
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
