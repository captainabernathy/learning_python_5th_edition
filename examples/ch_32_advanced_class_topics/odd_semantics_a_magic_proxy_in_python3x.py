# usage: python3 odd_semantics_a_magic_proxy_in_python3x.py

# class provides a single method, act()
class C:
    def act(self):
        print('spam')


# D is a C that overrides C's act() method
class D(C):
    def act(self):
        # NOTE: in python 3.X, DO NOT pass super() a refernce to self... since
        # super() references the calling object's superclass generically
        super().act()
        print('eggs')


# E is a C that inherits its act() method and also provides a method called
# method()
class E(C):
    def method(self):
        # NOTE: calling super() has no meaning outside of a method, AND self
        # is implicit in calls to super only
        proxy = super()
        print(proxy)  # <super: <class 'E'>, <E object>
        proxy.act()  # no args... implicitly calls superclass method


if __name__ == '__main__':
    print('code snippets from pages 1079-1080\n')

    X = D()
    X.act()  # spam, eggs
    print('')

    print(super)  # <class 'super'>
    # print(super())  # SystemError: no arguments... super() to what?
    print('')

    e = E()

    e.act()  # spam
    print('')

    e.method()  # <super: class 'E'>, <E object>, spam
