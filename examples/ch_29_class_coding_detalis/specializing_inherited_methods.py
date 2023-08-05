# usage: python3 specializing_inherited_methods.py

class Super:
    def method(self):
        print('in Super.method()')


# Sub inherits from Super
class Sub(Super):
    def method(self):  # Overrides Super's method()
        print('starting Sub.method()')
        Super.method(self)  # call Super's method() passing self directly
        print('ending Sub.method()')


if __name__ == '__main__':
    print('code snippets from pages 895-896\n')

    x = Super()  # build a Super instance
    x.method()  # in Super.method()
    print('')

    x = Sub()  # build a Sub instance
    x.method()
