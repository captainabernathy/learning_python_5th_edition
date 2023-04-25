class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(arg1,  arg2):  # simple function in 3.x
        return arg1 + arg2

    def normal(self, arg1, arg2):  # instance expected when called
        return self.data + arg1 + arg2


if __name__ == '__main__':
    print('code snippets from page 981\n')

    X = Selfless(2)
    print(X.normal(3, 4))  # 9... 2 + 3 + 4
    print(Selfless.selfless(3, 4))  # 7... 3 + 4
    print('')

    try:
        print(X.selfless(3, 4))  # can't be called from instance
    except TypeError:
        print('TypeError')
    print('')

    try:
        print(Selfless.normal(3, 4))  # can't be called from class
    except TypeError:
        print('TypeError')
