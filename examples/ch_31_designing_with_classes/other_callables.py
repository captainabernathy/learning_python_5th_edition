def square(arg):
    return arg ** 2


class Sum:  # callable instance
    def __init__(self, val):
        self.val = val

    def __call__(self, arg):  # overload () operator
        return self.val + arg


class Product:
    def __init__(self, val):
        self.val = val

    def method(self, arg):   # bound method
        return self.val * arg


class Negate:
    def __init__(self, val):
        self.val = -val

    def __repr__(self):
        return str(self.val)


if __name__ == '__main__':
    print('code snippets from pages 983-984\n')

    sobj = Sum(2)
    pobj = Product(3)

    actions = [square, sobj, pobj.method]
    for act in actions:
        print(act(5))  # 25 7 15... 5 ** 2, 5 + 2, 3 * 5
    print('')

    print(actions[-1](5))  # 15... 3 * 5
    print('')

    print([act(5) for act in actions])  # [25,7,15]... list comprehension
    print('')

    print(list(map(lambda act: act(5), actions)))  # [25,7,15]
    print('')

    actions = [square, sobj, pobj.method, Negate]
    for act in actions:
        print(act(5))  # 25 7 15 -5
    print('')

    print([act(5) for act in actions])  # [25,7,15,-5]
    print('')

    table = {act(5): act for act in actions}  # dictionary comprehension
    print(table)  # {25:<..>, 7:<...>, 15:<...>, -5:<...>}
    print('')

    for (key, value) in table.items():
        # 25 = <...>, 7 = <...>, 15 = <...>, -5 = <...>
        print('{0} =  {1}'.format(key, value))
