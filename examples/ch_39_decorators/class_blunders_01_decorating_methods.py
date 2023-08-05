# usage: python3 class_blunders_01_decorating_methods.py

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        # print(self)
        print(*args)
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    # NOTE: since tracer is a class, calls will not be bound to an instance
    # of Person... ERROR!!!
    @tracer
    def give_raise(self, percent):  # give_raise = tracer(Person.give_raise)
        self.pay *= (1.0 + percent)

    # NOTE: since tracer is a class, calls will not be bound to an instance
    # of Person... ERROR!!!
    @tracer
    def last_name(self):  # last_name = tracer(Person.last_name)
        return self.name.split()[-1]

    # for illustrative purposes
    def gr(self, percent):
        self.pay *= (1.0 + percent)

    def ln(self):
        return self.name.split()[-1]


if __name__ == '__main__':
    print('code snippets from page 1335\n')

    bob = Person('Bob Smith', 50000)

    try:
        bob.give_raise(.25)  # 0.25... call 1 to give_raise
    except TypeError as ex:
        print(ex)  # Person.give_raise() missing 1 requred positional argument:
                   # 'percent'
    print('')

    # below is what we want to happen... BUT, this is NOT what happens bc
    # the give_raise() method is bound to a tracer instance upon decoration,
    # so subsequent calls go through tracer and NOT bob
    tgr = tracer(Person.gr)
    tgr(bob, 0.25)  # <__main__.Person object at 0x...> 0.25
    print(bob.pay)  # 62500.00
    print('')

    # what ends up happening is this...
    try:
        tgr(0.25)  # 0.25... call 2 to gr
    except TypeError as ex:
        print(ex)  # Person.gr() missing 1 required positional argument:
                   # 'percent'
    print('')

    try:
        print(bob.last_name())
    except TypeError as ex:
        print(ex)  # Person.last_name() missing 1 required positional argument:
                   # 'self'
    print('')

    # similarly... what we want to happen
    tln = tracer(Person.ln)
    print(tln(bob))  # <__main__.Person object at 0x...>... call 1 to ln...
                     # Smith

    # BUT what actually happens is...
    try:
        tln()  # call 2 to ln
    except TypeError as ex:
        print(ex)  # Person.ln() missing 1 required positional argument: 'self'
    print('')
