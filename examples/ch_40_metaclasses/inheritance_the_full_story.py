# usage: python3 inheritance_the_full_story.py

# NOTE: in this example...
#   a) the instance inherits from all of its classes
#   b) the calss inherits from both classes and metaclasses
#   c) metaclasses inherit from higher metaclasses
#
# Overall
#   a) inheritance follows __bases__ before following a single __class__
#   b) normal instances have no __bases__
#   c) classes have both __bases__ and __class__ attributes... (both normal and
#      metaclasses)

class M1(type):
    attr1 = 1


class M2(M1):  # M2 gets __bases__, __class__, and __mro__
    attr2 = 2


class C1:
    attr3 = 3


class C2(C1, metaclass=M2):  # C2 gets __bases__, __class__, and __mro__
    attr4 = 4


if __name__ == '__main__':
    print('code snippets from pages 1429-1430\n')

    I1 = C2()  # I1 inherits class attributes from C2, and C1

    print(I1.attr3)  # 3
    print(I1.attr4)  # 4
    print('')

    print(C2.attr1)  # 1... C2. inherits class and metaclass attributes
    print(C2.attr2)  # 2
    print(C2.attr3)  # 3
    print(C2.attr4)  # 4
    print('')

    print(M2.attr1)  # 1... M2 inherits metaclass attributes
    print(M2.attr2)  # 2
    print('')

    # links followed at instance with no __bases__
    print(I1.__class__)  # <class '__main__.C2'>
    print(C2.__bases__)  # (<class '__main__.C1'>,)
    print('')

    # links followed at calss after __bases__
    print(C2.__class__)  # <class '__main__.M2'>
    print(M2.__bases__)  # (<class '__main__.M1'>,)
    print('')

    print(I1.__class__.attr1)  # 1... attr1 accessible through class
    print('')

    try:
        print(I1.attr1)  # attr1 not accessible through instance
    except AttributeError as ex:
        print(ex)
    print('')

    print(M2.__class__)  # <class 'type'>
    print('')

    # __bases__ tree from I1.__class__
    print([x.__name__ for x in C2.__mro__])  # ['C2','C1','object']
    print('')

    # __bases__ tree from C2.__class__
    print([x.__name__ for x in M2.__mro__])  # ['M2','M1','type','object']
    print('')

