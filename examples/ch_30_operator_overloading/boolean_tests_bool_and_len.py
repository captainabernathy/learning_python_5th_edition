# NOTE: in boolean contexts, python 3.X first tries __bool__() to obtain a
# direct boolean value, but if __bool__() is not defined, python then tries
# __len__() to infer a value based on an object's length... but 2.X tries
# __len__() first... if both __bool__() and __len__() are not defined, an
# object is considered vacuously true (for the most part)

class Truth1:
    def __bool__(self):
        return True


class Truth2:
    def __bool__(self):
        return False


class Truth3:
    def __len__(self):  # if __bool__ is missing, python falls back on __len__
        return 0


class Truth4:
    def __bool__(self):  # 3x tries __bool__ first
        return True

    def __len__(self):  # 2x tries __len__ first
        return 0


class Truth5:
    pass  # vacuously True


if __name__ == '__main__':
    print('code snippets from pages 956-957\n')
    X = Truth1()
    if X:
        print('yes!')  # yes!

    X = Truth2()
    print(bool(X))  # False

    X = Truth3()
    if not X:
        print('no!')  # no!... evaluates __len__() and interprets 0 as False

    X = Truth4()
    if X:
        print('yes!')  # yes!

    X = Truth5()
    print(bool(X))  # True... vacuously True
