# usage: python3 pseudoprivate.py

class C1:
    def meth1(self):
        self.__X = 88  # X is C1's

    def meth2(self):
        print(self.__X)  # becomes _C1__X in instance


class C2:
    def methA(self):
        self.__X = 99  # X is C2's

    def methB(self):
        print(self.__X)  # becomes _C2__X in instance


class C3(C1, C2):  # mixin
    pass


if __name__ == '__main__':
    print('code snippets from pages 976-977\n')

    MyInstance = C3()  # has to X names
    MyInstance.meth1()  # sets _C1__X = 88
    MyInstance.methA()  # sets _C2__X = 99
    print(MyInstance.__dict__)  # {'_C1__X': 88, '_C2__X': 99}
    MyInstance.meth2()  # 88
    MyInstance.methB()  # 99
