# usage: python3 string_representation_repr_and_str.py

class adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other  # in-place add... (bad form???)


# NOTE: __str__() is used by print() and by str() when it is defined...
# __repr__() is used by everything else

class addrepr(adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data  # convert to 'as-code' string


class addstr(adder):
    def __str__(self):
        return '[Value: %s]' % self.data  # convert to nice string


class addboth(adder):
    def __str__(self):
        return '[Value: %s]' % self.data  # user-friendly string

    def __repr__(self):
        return 'addboth(%s)' % self.data  # as-code string


if __name__ == '__main__':
    print('code snippets from pages 942-944\n')

    x = addrepr(2)
    print(x)  # addrepr(2)
    print(x + 1)  # None
    print(str(x), repr(x))  # addrepr(3) addrepr(3).. since __str__ not defined
    print('')

    x = addstr(3)
    print(x)  # [Value: 3]
    print(x + 1)  # None
    print(str(x), repr(x))  # [Value: 4] <__main__.addstr ...>  .. since
                            # __repr__() not defined
    print('')

    x = addboth(4)
    print(x)  # [Value: 4]... str() preferred by print()
    print(x + 1)  # None
    print(str(x), repr(x))  # [Value: 5] addboth(5)... __str__() and __repr__()
