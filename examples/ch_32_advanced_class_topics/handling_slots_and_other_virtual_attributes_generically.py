class Slotful:
    '''
    shows how to support slots as instance data
    '''
    __slots__ = ['a', 'b', '__dict__']

    def __init__(self, data):
        self.c = data


if __name__ == '__main__':
    print('code snippets from pages 1050\n')

    It = Slotful(3)
    It.a, It.b = 1, 2
    print(It.a, It.b, It.c)  # 1 2 3
    print('')

    print(It.__dict__)  # {'c': 3}
    print(It.__dict__['c'])  # 3

    # gettattr() fetches from both __slots__ and __dict__
    print(getattr(It, 'c'), getattr(It, 'a'))  # 3 1
    print('')

    # dir() captures everything
    print([x for x in dir(It) if not x.startswith('__')])  # ['a', 'b', 'c']
    print('')

    for a in (x for x in dir(It) if not x.startswith('__')):
        print(a, getattr(It, a))  # a 1, b 2, c 3
