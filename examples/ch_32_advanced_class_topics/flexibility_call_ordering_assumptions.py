class B:
    def __init__(self):
        print('B.__init__')
        super().__init__()


class C:
    def __init__(self):
        print('C.__init__')
        super().__init__()


# what if method call ording needs differ from MRO?
# NOTE: super() assumes that you really mean to pass method calls throughout
# all your classes per the MRO
class D(B, C):
    def __init__(self):
        print('D.__init__')
        C.__init__(self)
        B.__init__(self)


if __name__ == '__main__':
    print('code snippets from page 1091\n')

    # C gets instantiated twice bc B calls super(), which starts the chain of
    # propagation since B is first in the mro
    X = D()  # D.__init__, C.__init__, B.__init__, C.__init__
