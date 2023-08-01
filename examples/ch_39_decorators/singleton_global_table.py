instances = {}


def singleton_global_table(acls):  # runs On @singleton_global_table decoration
    # 3X and 2X: global table
    
    def on_call(*args, **kwargs):
        # On instance creation
        if acls not in instances:
            # One dict entry per class
            instances[acls] = acls(*args, **kwargs)
        return instances[acls]
    return on_call


@singleton_global_table
class Person:
    # Person = singleton_global_table(Person)
    # Rebinds Person to on_call()
    # on_call() remembers Person
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton_global_table
class Spam:
    # Spam = singleton_global_table(Spam)
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


Person1 = singleton_global_table(Person1)


class Spam1:
    def __init__(self, val):
        self.attr = val


Spam1 = singleton_global_table(Spam1)


if __name__ == '__main__':
    print('code snippets from page 1347\n')

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
