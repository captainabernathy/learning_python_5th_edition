# NOTE: 3X compatible only!

def singleton(aCls):  # runs on @singleton decoration
    instance = None

    def on_call(*args, **kwargs):
        nonlocal instance  # 3X only
        if instance is None:
            instance = aCls(*args, **kwargs)  # one scope per class
        return instance

    return on_call


@singleton
class Person:
    # Person = singleton(Person)
    # Rebinds Person to on_call()
    # on_call() remembers Person
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton
class Spam:
    # Spam = singleton(Spam)
    # Rebinds Spam to on_call
    # on_call remembers Spam
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
    print('code snippets from page 1348\n')

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
