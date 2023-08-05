# usage: python3 bound_methods_and_other_callable_objects.py

class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3


if __name__ == '__main__':
    print('code snippets from pages 982-983\n')

    x = Number(2)
    y = Number(3)
    z = Number(4)

    print(x.double())  # 4
    print('')

    acts = [x.double, y.double, y.triple, z.double]  # list of bound methods
    for act in acts:
        print(act())  # 4 6 9 8
    print('')

    bound = x.double
    # <__main__.Number object at 0x...> <function Number.double at 0x...>
    print(bound.__self__, bound.__func__)  # both have same address
    print('')
    print(bound.__self__.base)  # 2
    print(bound())  # 4... calls x.double()
