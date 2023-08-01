# call tracer decorator for both functions and methods

# NOTE: define tracer as a function, NOT a class with __call__()... else
# self will be the tracer decorator instance only
def tracer(func):
    calls = 0

    def on_call(*args, **kwargs):
        nonlocal calls  # NOTE: 3X only
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return on_call


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def give_raise(self, percent):  # give_raise = tracer(Person.give_raise)
        self.pay *= (1.0 + percent)  # on_call remembers give_raise

    @tracer
    def last_name(self):  # last_name = tracer(Person.last_name)
        return self.name.split()[-1]  # on_call remembers last_name

    # for illustrative purposes
    def gr(self, percent):
        self.pay *= (1.0 + percent)

    def ln(self):
        return self.name.split()[-1]


@tracer
def spam(a, b, c):  # spam = tracer(spam)
    print(a + b + c)


@tracer
def eggs(N):  # eggs = tracer(eggs)
    return 2 ** N


if __name__ == '__main__':
    print('code snippets from pages 1336-1337\n')

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

    sue.give_raise(.10)  # call 1 to give_raise...  runs on_call(sue, .10)
    print(int(sue.pay))  # 110000
    print('')

    # here, since tracer is a function and NOT a class, there are no subsequent
    # issues with self or forwarding arguments
    gr = tracer(Person.gr)
    gr(sue, 0.10)  # call 1 to gr
    print(int(sue.pay))  # 121000
    print('')
 
    print(bob.last_name())  # call 1 to last_name... Smith
    print('')

    # again... no issues
    ln = tracer(Person.ln)
    print(ln(bob))  # call 1 to ln... Smith
    print('')

    print(sue.last_name())  # call 2 to last_name... Jones
    print('')

    # and again... no issues
    print(ln(sue))  # call 2 to ln... Jones
    print('')
