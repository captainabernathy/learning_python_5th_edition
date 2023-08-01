class singleton:
    # 3X and 2X classes
    def __init__(self, acls):  # runs on @singleton decoration
        self.acls = acls
        self.instance = None

    def __call__(self, *args, **kwargs):
        # On instance creation
        if self.instance is None:
            # One instance per calss
            self.instance = self.acls(*args, **kwargs)
        return self.instance


@singleton
class Person:
    # Person = singleton(Person)
    # Rebinds Person to __call__()
    # __call__() remembers Person
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton
class Spam:
    # Spam = singleton(Spam)
    # Rebinds Spam to __call__()
    # __call__() remembers Spam
    def __init__(self, val):
        self.attr = val


# for illustrative purposes...
class Person1:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


Person1 = singleton(Person1)


class Spam1:
    def __init__(self, val):
        self.attr = val


Spam1 = singleton(Spam1)


if __name__ == '__main__':
    print('code snippets from pages 1348-1349\n')

    bob = Person('Bob', 40, 10)
    print(bob.name, bob.pay())  # Bob 400
    print('')

    sue = Person('Sue', 50, 20)
    print(sue.name, sue.pay())  # Bob 400
    print('')

    X = Spam(val=42)
    Y = Spam(99)
    print(X.attr, Y.attr)  # 42 42
    
    print('')
    print('-' * 80)
    print('')

    bob1 = Person1('Bob', 40, 10)
    print(bob1.name, bob1.pay())  # Bob 400
    print('')

    sue1 = Person1('Sue', 50, 20)
    print(sue1.name, sue1.pay())  # Bob 400
    print('')

    X1 = Spam1(val=42)
    Y1 = Spam1(99)
    print(X1.attr, Y1.attr)  # 42 42
    print('')
