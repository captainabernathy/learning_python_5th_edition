# NOTE: attribute descriptors refer to  __get__() and __set__() methods that
# are assigned to class attributes (and inherited by instances) and intercept
# read and write access to specific attributes

class AgeDesc(object):
    def __get__(self, instance, owner):
        return 40

    def __set__(self, instance, value):
        instance._age = value


class descriptors(object):
    age = AgeDesc()


if __name__ == '__main__':
    print('code snippets from page 1054\n')

    X = descriptors()

    print(X.age)  # 40... calls AgeDesc.__get__()
    print('')

    X.age = 42  # calls AgeDesc.__set__()... sets X._age
    print(X._age)  # 42... normal access... no descriptor for _age
