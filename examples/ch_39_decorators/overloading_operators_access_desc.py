from access_desc import private


@private('age')
class Person:
    def __init__(self):
        self.age = 42

    def __str__(self):
        return 'Person: ' + str(self.age)

    def __add__(self, yrs):
        self.age += yrs


if __name__ == '__main__':
    print('code snippets from page 1373\n')

    X = Person()
    try:
        print(X.age)
    except TypeError as ex:
        print(ex)  # private attribute fetch: age
    print('')

    # __str__() overloaded in (mixin) super class provided to proxy class in
    # access_control(), delegates to wrapped object
    print(X)  # Person: 42
    print('')

    # __add__() overloaded in (mixin) super class provided to proxy class in
    # access_control(), delegates to wrapped object
    X + 10

    print(X)  # Person: 52
    print('')
