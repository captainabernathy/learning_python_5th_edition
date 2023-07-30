# tests various attribute types and built-in operations on instances of classes
# containing __getattr__() and __getattribute__() methods

# NOTE: Operator overloading methods implicitly run by built-in operations are
# never routed through either attribute interception methods (__getattr__(),
# __getattribute__())in 3.X... bc new-style classes search for such attributes
# in classes and skip instance lookup entirely... however normally named
# attributes do not

class GetAttr:
    eggs = 88  # class attribute

    # constructor builds a GetAttr with its spam attribute set to 77
    def __init__(self):
        self.spam = 77  # instance attribute

    # len() operator overloaded for GetAttr instances
    def __len__(self):
        print('__len__: 42')
        return 42

    # in 3X:
    #   * intercepts undefined attribute lookups
    #   * intercepts explict calls to undefined built-in operators
    #   * does NOT intercept implict calls to __getitem__(), __add__(), and
    #     __call__()... ie: obj[i], obj + other, obj()
    #   * does NOT intercept explict or implict calls to __str__() and
    #     __repr__()
    #   * does NOT intercept implicit and explicit calls to defined attributes
    #     and built-in operators... ie: len(obj), obj.__len__(), obj.known
    # in 2X:
    #   * intercepts undefined attribute lookups
    #   * intercepts implicit calls to __getitem__(), __add__(), and __call__()
    #     ie: obj[i], obj + other, obj()
    #   * intercepts implict and explict calls to __str__() and __repr()
    #   * does NOT intercept implicit and explict calls to defined attributes
    #     and built-in operators... ie: len(obj), obj.__len__(), obj.known
    def __getattr__(self, attr):
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


class GetAttribute(object):
    eggs = 88  # class attribute

    # constructor builds a GetAttribute with its spam attribute set to 77
    def __init__(self):
        self.spam = 77  # instance attribute

    # len() operator overloated for GetAttribute instances
    def __len__(self):
        print('__len__: 42')
        return 42

    # in 3X:
    #   * intercepts defined and undefined attribute lookups
    #   * intercepts explicit calls to defined and undefined operators...
    #     ie: obj.__len__(), obj.__call__(), obj.__str__()
    #   * does NOT intercept implicit calls to __getitem__(), __add__(), and
    #     __call__()... ie: obj[i], obj + other, obj()
    #   * does NOT intercept implicit calls to defined operators...
    #     ie: len(obj)
    #   * does NOT intercept implicit calls to __str__() and __repr__()
    # in 2X:
    #   * intercepts defined and undefined attribute lookups
    #   * intercepts explict calls to defined and undefined operators
    #     ie: obj.__len__(), obj.__call__(), obj.__str__()
    #   * does NOT intercept implicit calls to __getitem__(), __add__(), and
    #     __call__()... ie: obj[i], obj + other, obj()
    #   * does NOT intercept implcit calls to defined operators...
    #     ie: len(obj)
    #   * does NOT intercept implict calls to __str__() and __repr__()
    def __getattribute__(self, attr):
        print('getattribute: ' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None


if __name__ == '__main__':
    print('code snippets from pages 1292-1294\n')

    for Class in GetAttr, GetAttribute:
        print('\n' + Class.__name__.ljust(50, '='))

        X = Class()
        X.eggs  # Class attribute
        X.spam  # instance attribute
        X.other  # undefined attribute
        len(X)  # __len__() explicitly defined operator

        try:
            X[0]  # implicit call to __getitem__()
        except TypeError:
            print('fail []')

        try:
            X + 99  # implicit call to __add__()
        except TypeError:
            print('fail +')

        try:
            X()  # implicit call to __call__()
        except TypeError:
            print('fail ()')

        X.__len__()  # explicit call to __len__()
        X.__call__()  # explicit call to __call__()... not inherited
        print(X.__str__())  # explicit call to __str__()... inherited from type
        print(X)  # implicit call to __str__() via built-in
    print('')
