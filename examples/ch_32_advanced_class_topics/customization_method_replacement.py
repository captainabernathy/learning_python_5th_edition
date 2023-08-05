# usage: python3 customization_method_replacement.py

class A1:
    def method(self):
        print('A1.method')
        super().method()


class B1(A1):
    def method(self):
        print('B1.method')
        super().method()


class C1:
    def method(self):
        print('C1.method')  # no super().method()


class D1(B1, C1):
    def method(self):
        print('D1.method')
        super().method()


# what if a class needs to replace a super's default entirely?
# NOTE: replacement breaks the call chain
class B2(A1):
    def method(self):
        print('B2.method')  # drops super to replace A's method


class D2(B2, C1):
    def method(self):
        print('D2.method')
        super().method()


class D3(B2, C1):
    def method(self):  # explicit calls are required to maintain call chain
        print('D3.method')
        B2.method(self)
        C1.method(self)


if __name__ == '__main__':
    print('code snippets from page 1092\n')

    # NOTE: the universal deployment expectations of super() make it difficult
    # for a single class to replace (override) an inherited method altogether
    X = D1()

    # dispatch to all per MRO automatically
    X.method()  # D1.method, B1.method, A1.method, C1.method
    print('')

    X = D2()
    # C1 not called since B2 breaks chain of propagation
    X.method()  # D2.method B2.method
    print('')

    X = D3()
    X.method()  # D3.method B2.method C1.method
