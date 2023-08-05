# usage: python3 generalizing_for_public_declarations.py

from access2 import private
from access2 import public


@private('age')
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


@public('name')
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person11:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person22:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    print('code snippets from pages 1365-1366\n')

    X = Person1('Bob', 40)
    print(X.name)  # Bob
    print('')

    X.name = 'Sue'
    print(X.name)  # Sue
    print('')

    try:
        print(X.age)
    except TypeError as ex:
        print(ex)  # private attribute fetch: age
    print('')

    try:
        X.age = 'Tom'
    except TypeError as ex:
        print(ex)  # private attribute fetch: age
    print('')

    X = Person2('bob', 40)
    print(X.name)  # bob
    print('')

    X.name = 'Sue'
    print(X.name)  # Sue
    print('')

    try:
        print(X.age)
    except TypeError as ex:
        print(ex)  # private attribute fetch: age
    print('')

    try:
        X.age = 'Sue'
    except TypeError as ex:
        print(ex)  # private attribute fetch: age
    print('')

    print('-' * 80)
    print('')

    X1 = private('age')(Person11)('Bob', 40)

    print(X1.name)  # Bob
    print('')

    X1.name = 'Sue'
    print(X1.name)  # Sue
    print('')

    try:
        print(X1.age)
    except TypeError as ex:
        print(ex)  # private attribute fetch: age
    print('')

    try:
        X1.age = 'Tom'
    except TypeError as ex:
        print(ex)  # private attribute fetch: age
    print('')

    X1 = public('name')(Person22)('bob', 40)

    print(X1.name)  # bob
    print('')

    X1.name = 'Sue'
    print(X1.name)  # Sue
    print('')

    try:
        print(X1.age)
    except TypeError as ex:
        print(ex)  # private attribute fetch: age
    print('')

    try:
        X1.age = 'Sue'
    except TypeError as ex:
        print(ex)  # private attribute fetch: age
    print('')
