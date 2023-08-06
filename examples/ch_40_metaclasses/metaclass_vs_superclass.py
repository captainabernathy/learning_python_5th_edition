# usage: python3 metaclass_vs_superclass.py

class A1(type):
    attr = 1


# B1 is a meta instance and acquires the meta attribute attr, which is NOT
# available for inheritance by B1's own instances
class B1(metaclass=A1):
    pass


# NOTE: since A2 is a normal class, then names inherited from A2 are available
# to instances of classes that inherit from A2
class A2:
    attr = 1


class B2(A2):
    pass


# NOTE: when the same name is available in as both a metaclass and superclass
# attribute, the name inherited from the superclass is used as opposed to the
# name acquired from the metaclass instance
class M3(type):
    attr = 1


class A3:
    attr = 2


class B3(A3, metaclass=M3):
    pass


# NOTE: python checks the __dict__ of each class on the MRO before falling back
# on metaclass acquisition
class M4(type):
    attr = 1


class A4:
    attr = 2


class B4(A4):
    pass


class C4(B4, metaclass=M4):
    pass


if __name__ == '__main__':
    print('code snippets from pages 1427-1429\n')

    I1 = B1()  # I1 inherits from a class... but NOT a meta class

    print(B1.attr)  # 1
    print('')

    try:
        print(I1.attr)  # ERROR!
    except AttributeError as ex:
        print(ex)  # 'B1' objevt has not attribute 'attr'
    print('')

    print('attr' in B1.__dict__)  # False
    print('attr' in A1.__dict__)  # True
    print('')

    I2 = B2()  # I2 inherits from class and supers

    print(B2.attr)  # 1... attr inherited from A2
    print(I2.attr)  # 1
    print('')

    print('attr' in B2.__dict__)  # False
    print('attr' in A2.__dict__)  # True
    print('')

    I3 = B3()

    print(B3.attr)  # 2... inherited from A3
    print(I3.attr)  # 2
    print('')

    print('attr' in B3.__dict__)  # False
    print('attr' in A3.__dict__)  # True
    print('attr' in M3.__dict__)  # True
    print('')

    I4 = C4()
    
    print(C4.attr)  # 2... inherited from A4
    print(I4.attr)  # 2
    print('')

    print([x.__name__ for x in C4.__mro__])  # ['C4','B4','A4','object']
    print('')

    # NOTE: that instance inheritance does NOT follow a class's __class__
    # attribute, but instead restricts its scope to the __dict__ of each class
    # in a tree per the MRO (following __bases__ at each class only, and using
    # the instance's __class__ link once)

    # instance's class... followed by inheritance
    print(I4.__class__)  # <class '__main__.C4'>
    print('')

    # super classes... followed by inheritance
    print(C4.__bases__)  # (<class '__main__.B4'>,)

    # metaclass: followed by instance acquisition
    print(C4.__class__)  # <class '__main__.M4'>
    print('')

    print(C4.__class__.attr)  # 1... how to get to metaclass attribute

