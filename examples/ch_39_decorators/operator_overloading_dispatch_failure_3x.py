# usage: python3 operator_overloading_dispatch_failure_3x.py

from access2 import private


@private('age')
class Person:
    def __init__(self):
        self.age = 42

    def __str__(self):
        return 'Person: ' + str(self.age)

    def __add__(self, yrs):
        self.age += yrs


if __name__ == '__main__':
    print('code snippets from pages 1369-1370\n')

    X = Person()
    try:
        print(X.age)
    except TypeError as ex:
        print(ex)  # private attribute fetch: age
    print('')

    # doesn't call __str__... print calls the default display inherited from
    # the class type (the implied object)
    # <access2.access_control.<local>.on_decorator.<locals>.on_instance ....>
    print(X)
    print('')

    try:
        #  '+' generates an error bc no default is inherited
        X + 10
    except TypeError as ex:
        print(ex)  # unsupported operand type(s) for +: 'on_instance' and 'int'
    print('')

    # NOTE: explicit, direct calls to overloaded methods ARE routed to
    # __getattr__()
    X.__add__(10)
    print(X._on_instance__wrapped.age)  # 52
    print('')

    print(X._on_instance__wrapped.__str__())  # Person: 52
