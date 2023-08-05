# usage: python3 custom_print_displays_01.py

class MyBad1(Exception):
    pass


# NOTE: to provide a custom message to an Exception class, overload either the
# __str__() or __repr__() method
class MyBad2(Exception):
    def __str__(self):
        return 'Always look on the bright side of life...'


# it is preferable to overload __str__() in order to avoid python calling the
# superclass's built-in __str__() method by default
class MyBad3(Exception):
    def __repr__(self):  # probably won't get called
        return 'Never look on the bright side of life...'


if __name__ == '__main__':
    print('code snippets from pages 1173-1174\n')

    try:
        raise MyBad1('Sorry--my mistake!')
    except MyBad1 as ex:
        print(ex)  # 'Sorry--my mistake!'
    print('')

    try:
        raise MyBad2()
    except MyBad2 as ex:
        print(ex)  # Always look on the bright side of life...
    print('')

    try:
        raise MyBad3('blah')
    except MyBad3 as ex:
        print(repr(ex))  # Never look on the bright side of life...
        print(ex)  # blah... calls superclass's str()
        print(ex.__repr__())  # Never look on the bright side of life...
