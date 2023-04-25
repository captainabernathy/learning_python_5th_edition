from listinstance import ListInstance


class Super:
    def __init__(self):
        self.data1 = 'spam'  # instance attrs

    def ham(self):  # bound method
        pass


class Sub(Super, ListInstance):  # mixin
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'  # more instance attrs
        self.data3 = 42

    def spam(self):  # bound method
        pass


if __name__ == '__main__':
    print('code snippets from page 993\n')

    X = Sub()
    print(X)  # calls ListInstance's __str__() method
