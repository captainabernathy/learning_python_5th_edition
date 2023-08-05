# usage: python3 desc_state_inst.py

# NOTE: this descriptor class manages data on a client instance instead of
# itself, which allows for data that can vary per client class instance

class InstState:  # use (object) in 2X
    # returns instance's _X attribute times 10
    def __get__(self, instance, owner):
        print('InstState get')
        return instance._X * 10

    # sets instance's _X attribute to value
    def __set__(self, instance, value):
        print('InstState set')
        instance._X = value


# Client class
class CalcAttrs:
    X = InstState()  # assigns an InstState descriptor to the class attribute X
    Y = 3            # initializes class attribute Y

    # constructor builds a CalcAttrs with its _X member initialized to 2 and
    # its Z member initialized to 4
    def __init__(self):
        self._X = 2  # sets instance's _X attribute
        self.Z = 4  # initializes instance attribute Z


if __name__ == '__main__':
    print('code snippets from pages 1276-1277\n')

    obj = CalcAttrs()
    print(obj.X, obj.Y, obj.Z)  # InstState get... 20, 3, 4
    print('')

    obj.X = 5  # InstState set
    CalcAttrs.Y = 6
    obj.Z = 7
    print(obj.X, obj.Y, obj.Z)  # InstState get... 50, 6, 7
    print('')

    obj2 = CalcAttrs()
    print(obj2.X, obj2.Y, obj2.Z)  # InstState get... 20, 6, 4
    print('')
