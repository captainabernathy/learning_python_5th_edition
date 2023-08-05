# usage: python3 calltracer_desc_02.py

class tracer(object):  # a decorator + descriptor
    def __init__(self, func):  # runs on @tracer decorator
        self.calls = 0
        self.func = func  # save func for later calls

    def __call__(self, *args, **kwargs):  # runs on calls to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):  # runs on method attribute lookup
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)
        # print('self: %s\ninstance: %s\nowner %s\n' % (self, instance, owner))
        return wrapper  # returns a wrapper instance


@tracer
def spam(a, b, c):  # spam = tracer(spam)
    print(a + b + c)  # uses __call__ only


@tracer
def eggs(N):
    return 2 ** N


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def give_raise(self, percent):  # give_raise = tracer(Person.give_raise)
        self.pay *= (1.0 + percent)  # makes give_raise a descriptor

    @tracer
    def last_name(self):  # last_name = tracer(Person.last_name)
        return self.name.split()[-1]

    # for illustrative purposes...
    def gr(self, percent):
        self.pay *= (1.0 + percent)

    def ln(self):
        return self.name.split()[-1]


if __name__ == '__main__':
    print('code snippets from page 1338\n')

    spam(1, 2, 3)  # call 1 to spam... 6
    print('')

    spam(a=4, b=5, c=6)  # call 2 to spam... 15
    print('')

    print(eggs(32))  # call 1 to eggs... 4294967296
    print('')

    print('methods...')

    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)

    print(bob.name, sue.name)  # Bob Smith Sue Jones
    print('')

    sue.give_raise(0.10)  # call 1 to give_raise
    print(int(sue.pay))  # 110000
    print('')

    # illustrating w/explicit calls
    tgr = tracer(Person.gr)
    wsgr = tgr.__get__(sue, Person)
    # wrapper(tgr, sue)
    wsgr(0.10)  # call 1 to gr
    print(int(sue.pay))  # 121000
    print('')

    print(bob.last_name())  # call 1 to last_name... Smith
    print('')

    # illustrating w/explicit calls
    tln = tracer(Person.ln)
    wbln = tln.__get__(bob, Person)
    print(wbln())  # call 1 to ln... Smith
    print('')

    print(sue.last_name())  # call 2 to last_name... Jones
    print('')

    # illustrating w/explicit calls
    wsln = tln.__get__(sue, Person)
    print(wsln())  # call 2 to ln... Jones
    print('')

