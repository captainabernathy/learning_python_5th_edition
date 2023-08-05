# usage: python3 multiple_inheritance_mixin_classes.py

from listinstance import ListInstance


class Spam(ListInstance):
    def __init__(self):
        self.data1 = 'food'


if __name__ == '__main__':
    print('code snippets from page 992\n')

    x = Spam()
    print(x)  # calls ListInstance's __str__() method
