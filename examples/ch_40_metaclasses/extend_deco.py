# usage: python3 extend_deco.py

def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


# can be used as a decorator to simulate a metaclass
def Extender(aClass):
    aClass.eggs = eggsfunc
    aClass.ham = hamfunc
    return aClass


@Extender
class Client1:  # Client1 = Extender(Client1)
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


@Extender
class Client2:
    value = 'ni?'


if __name__ == '__main__':
    print('code snippets from page 1442\n')

    X = Client1('Ni!')

    print(X.spam())  # Ni!Ni!
    print(X.eggs())  # Ni!Ni!Ni!Ni!
    print(X.ham('bacon'))  # baconham
    print('')

    Y = Client2()

    print(Y.eggs())  # ni?ni?ni?ni?
    print(Y.ham('bacon'))  # baconham
    print('')

