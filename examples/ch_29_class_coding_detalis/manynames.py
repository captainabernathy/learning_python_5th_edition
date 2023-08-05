# usage: python3 manynames.py

X = 11  # global (module) name/attribute


def f():
    print(X)  # accesses global X (11)


def g():
    X = 22  # local X (function)... hides module's X
    print(X)  # 22


class C:
    X = 33  # class attribute C.X

    def m(self):
        X = 44  # local X (method)... assigned but never used
        self.X = 55  # sets instance's X attribute (instance.X)


if __name__ == '__main__':
    print('code snippets from page 902\n')

    print(X)  # 11
    f()   # 11
    g()  # 22
    print(X)  # 11
    print('')

    obj = C()
    print(obj.X)  # 33... class attribute

    obj.m()  # attaches attribute name X to instance
    print(obj.X)  # 55
    print(C.X)  # 33... class attribute
