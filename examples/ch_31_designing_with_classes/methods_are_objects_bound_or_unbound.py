# usage: python3 methods_are_objects_bound_or_unbound.py

class Spam:
    def doit(self, message):
        print(message)


class Eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1  # bound method object
        x(42)


if __name__ == '__main__':
    print('code snippets from pages 979-980\n')

    obj1 = Spam()
    obj1.doit('hello world')  # call object's method
    print('')

    x = obj1.doit  # bound method... method is bound to an instance
    x('hello world')  # same as obj1.doit()
    print('')

    t = Spam.doit  # unbound method... method is not bound to an instance
    t(obj1, 'howdy')  # pass in instance (if the method expects one in 3X)
    print('')

    Eggs().m2()  # 42
