# usage: python3 metaclass_03.py

print('code snippets from page 1420\n')


# NOTE: in principle, any callable object cn be used as a metaclass provided
# that it accepts the arguments passeed and returns an object compatible with
# the intended class

# a simple, object factory function that serves the same role as a type
# subclass
def MetaFunc(classname, supers, classdict):
    print('In MetaFunc:', classname, supers, classdict, sep='\n...')
    print('')
    return type(classname, supers, classdict)


class Eggs:
    pass


print('making class...')


# as soon as the class statement is processed...
# In MetaFunc:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1,
# 'meth': <function Spam.meth at 0x...>}
class Spam(Eggs, metaclass=MetaFunc):
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
