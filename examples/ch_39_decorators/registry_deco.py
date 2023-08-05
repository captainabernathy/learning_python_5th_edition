# usage: python3 registry_deco.py

# Registering decorated objects to an API
from __future__ import print_function


registry = {}


def register(obj):
    '''
    both class and func decorator
    '''
    registry[obj.__name__] = obj  # add obj to registry and return it
    return obj


@register
def spam(x):
    # spam = register(spam)
    return x ** 2


@register
def ham(x):
    # ham = register(ham)
    return x ** 3


@register
class Eggs:
    # Eggs = register(Eggs)
    def __init__(self, x):
        self.data = x ** 4

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    print('code snippets from pages 1358-1359\n')

    print('Registry:')
    # spam => <function spam at 0x...> <class 'function'>
    # ham => <function ham at 0x...> <class 'function'>
    # Eggs => <class '__main__.Eggs'> <class 'type'>
    for name in registry:
        print(name, '=>', registry[name], type(registry[name]))
    print('')

    # Invoke objects manually
    # Later calls not intercepted
    print('Manual calls:')
    print(spam(2))  # 4
    print(ham(2))  # 8
    X = Eggs(2)
    print(X)  # 16
    print('')

    print('Registry calls:')
    # spam => 4
    # ham => 8
    # Eggs => 16
    for name in registry:
        print(name, '=>', registry[name](2))  # Invoke from registry
    print('')
