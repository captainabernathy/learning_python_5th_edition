# usage: python3 function_decorator_basics.py

from spam_static_deco import Spam
from bothmethods_decorators import Methods


if __name__ == '__main__':
    print('code snippets from pages 1071-1072\n')

    # build some Spam objects
    a = Spam()
    b = Spam()
    c = Spam()

    # static method called through class
    Spam.print_num_instances()  # Number of instances created: 3

    # static method called through instance
    a.print_num_instances()  # Number of instances created: 3
    print('')

    # build a Methods object
    obj = Methods()

    # instance method called from object
    obj.imeth(1)  # [<bothmethods_decorators.Methods object at 0x...>, 1]

    # instance method called through class with instance passed explicitly
    # [<bothmethods_decorators.Methods object at 0x...>, 1]
    Methods.imeth(obj, 1)
    print('')

    # static method called through instance
    obj.smeth(2)  # [2]

    # static method called through class
    Methods.smeth(22)  # [22]
    print('')

    # class method called through instance
    obj.cmeth(3)  # [<class 'both_decorators.Methods'>, 3]

    # class method called through class
    Methods.cmeth(33)  # [<class 'both_decorators.Methods'>, 33]
    print('')

    # access class property
    print(obj.name)  # Bob Methods

    try:
        obj.name = 'Not Bob'
    except AttributeError as ex:
        print(ex)  # can't set attribute name

