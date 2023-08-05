# usage: python3 specialize.py

class Super:
    def method(self):
        print('in Super.method()')

    # NOTE: delegate expects the method acition() to be defined in a subclass
    def delegate(self):
        self.action()  # expected to be defined in a subclass


class Inheritor(Super):  # inherits method() verbatim
    pass


class Replacer(Super):  # replaces method() completely
    def method(self):
        print('in Replacer.method()')


class Extender(Super):  # extends method()'s behavior
    def method(self):
        print('starting Extender.method()')
        Super.method(self)
        print('ending Extender.method()')


class Provider(Super):  # provide's delegate()-ed method... action()
    def action(self):
        print('in Provider.action()')


if __name__ == '__main__':
    print('code snippets from pages 896-897\n')

    # instances are constructed automatically in for loop
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()  # chain method call to instance

    print('\nProvider...')
    x = Provider()  # build a Provider instance
    x.delegate()  # in Provider.action()... delegate() calls action()
