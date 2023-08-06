# usage: python3 extended_manual.py

class Client1:
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2:
    value = 'ni?'


def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


if __name__ == '__main__':
    print('code snippets from pages 1438-1439\n')

    # add new methods to classes manually
    Client1.eggs = eggsfunc
    Client1.ham = hamfunc

    Client2.eggs = eggsfunc
    Client2.ham = hamfunc

    X = Client1('Ni!')

    print(X.spam())  # Ni!Ni!
    print(X.eggs())  # Ni!Ni!Ni!Ni!
    print(X.ham('bacon'))  # baconham
    print('')

    Y = Client2()
    print(Y.eggs())  # ni?ni?ni?ni?
    print(Y.ham('bacon'))  # baconham
    print('')

