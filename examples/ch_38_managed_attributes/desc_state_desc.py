# NOTE: this descriptor class attaches information to its own instance so that
# it doesn clash with information on a client instance... BUT the descriptor's
# information is shared amongst its clients

class DescState:  # use (object) in 2X
    # constructor builds a DescState with its value member initialized to value
    def __init__(self, value):
        self.value = value

    # returns this DescState's value times 10
    def __get__(self, instance, owner):
        print('DescState get')
        return self.value * 10

    # sets this DescState's value member to value
    def __set__(self, instance, value):
        print('DescState set')
        self.value = value


# Client class
class CalcAttrs:
    X = DescState(2)  # assigns a DescState descriptor to the class attribute X
    Y = 3  # initializes class attribute Y

    # constructor builds a CalcAttrs with its Z attribute initialized to 4
    def __init__(self):
        self.Z = 4  # initializes instance attribute Z to 4


if __name__ == '__main__':
    print('code snippets from page 1275\n')

    obj = CalcAttrs()
    print(obj.X, obj.Y, obj.Z)  # DescState get... 20, 3, 4
    print('')

    # set descriptor attribute
    obj.X = 5  # DescState set... DescState's __set__()
    CalcAttrs.Y = 6  # set class attribute
    obj.Z = 7  # set instance attribute
    print(obj.X, obj.Y, obj.Z)  # DescState get... 50, 6, 7
    print('')

    # shares class level descriptor (X) and attribute (Y) with other instances
    obj2 = CalcAttrs()
    print(obj2.X, obj2.Y, obj2.Z)  # DescState get... 50, 6, 4
    print('')
