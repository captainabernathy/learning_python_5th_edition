# usage: python2 metaclass_01_2x.py

from __future__ import print_function


print('code snippets from page 1417-1418\n')


# meta class coded the same
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict,
              sep='\n...')
        print('')
        return type.__new__(meta, classname, supers, classdict)


class Eggs(object):  # new style class
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
class Spam(Eggs, object):
    __metaclass__ = MetaOne  # define __metaclass__ attribute in 2X
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
