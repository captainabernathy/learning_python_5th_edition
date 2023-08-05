# usage: python3 desc_computed.py

class DescSquare:
    # constructor builds a DescSquare with its value attribute initialized to
    # start
    def __init__(self, start):
        self.value = start

    # returns the square of this DescSquare's value attribute
    def __get__(self, instance, owner):
        return self.value ** 2

    # sets this DescSquare's value attribute to value
    def __set__(self, instance, value):
        self.value = value


class Client1:
    # assigns a DescSquare descriptor to the attribute X
    X = DescSquare(3)


class Client2:
    # assigns a DescSquare descriptor to the attribute X
    X = DescSquare(32)


if __name__ == '__main__':
    print('code snippets from page 1274\n')

    c1 = Client1()
    c2 = Client2()

    print(c1.X)  # 9... DescSquare.__get__()
    print('')

    c1.X = 4  # DescSquare.__set__()
    print(c1.X)  # 16
    print('')

    print(c2.X)  # 1024... DescSquare.__get__()
    print('')
