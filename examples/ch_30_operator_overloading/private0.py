# usage: python3 private0.py

class PrivateExc(Exception):
    pass  # will cover this later in the book


class Privacy:
    def __setattr__(self, attrname, value):  # on self.attrname = value
        if attrname in self.privates:
            raise PrivateExc(attrname, self)  # make, raise user-defined except
        else:
            self.__dict__[attrname] = value  # avoid loops by using dict keys


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


if __name__ == '__main__':
    print('code snippets from pages 941-942\n')

    x = Test1()
    y = Test2()
    x.name = 'Bob'  # ok
    print(x.name)  # Bob

    try:
        y.name = 'Sue'  # whoops... name attribute in y's __dict__
    except PrivateExc:
        print('PrivateExc')
    print('')

    y.age = 30  # ok... age attribute not in y's __dict__
    print(y.age)
    try:
        x.age = 40  # whoops... age added to y's __dict__ above
    except PrivateExc:
        print('PrivateExc')
    print('')
