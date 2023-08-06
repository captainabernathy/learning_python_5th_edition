# usage: python3 extended_meta.py

def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)


# NOTE: client classes are extended with new methods when they are
# instances of a metaclass that performs the augmentation
class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2(metaclass=Extender):
    value = 'ni?'


if __name__ == '__main__':
    print('code snippets from page 1440\n')

    X = Client1('Ni!')

    print(X.spam())  # Ni!Ni!
    print('')

    print(X.eggs())  # Ni!Ni!Ni!Ni!
    print('')

    print(X.ham('bacon'))  # baconham
    print('')

    Y = Client2()

    print(Y.eggs())  # ni?ni?ni?ni?
    print('')

    print(Y.ham('bacon'))  # baconham
    print('')

