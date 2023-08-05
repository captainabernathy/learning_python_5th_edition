# usage: python3 changing_mutable_class_attributes_can_have_side_effects_too.py

class C:
    shared = []  # Mutable class attribute

    def __init__(self):
        self.perobj = []  # instance attribute


if __name__ == '__main__':
    print('code snippets from page 1102\n')

    x = C()
    y = C()
    print(x.shared, y.perobj)  # [] []
    print('')

    x.shared.append('spam')
    x.perobj.append('eggs')
    print(x.shared, x.perobj)  # ['spam'] ['eggs']
    print('')

    print(y.shared, y.perobj)  # ['spam'] []
    print('')

    y.shared.append('ham')  # NOTE: append() changes a class attribute in place
    print(x.shared, x.perobj)  # ['spam'] ['eggs']
    print(y.shared, y.perobj)  # ['ham'] []
    print('')

    print(C.shared)  # ['spam', 'ham']... set by x
    print('')

    x.shared = ['bacon']  # assignment creates or changes an instance attribute

    print(x.shared, x.perobj)  # ['bacon'] ['eggs']
    print(y.shared, y.perobj)  # ['spam','ham'] []
    print(C.shared)  # ['spam','ham']
    print('')

    C.shared.append('cheese')
    print(x.shared, x.perobj)  # ['bacon'] ['eggs']
    print(y.shared, y.perobj)  # ['spam','ham','cheese'] []
    print(C.shared)  # ['spam','ham','cheese']
    print('')

    C.shared = ['fruit']
    print(x.shared, x.perobj)  # ['bacon'] ['eggs']
    print(y.shared, y.perobj)  # ['fruit'] []
    print(C.shared)  # ['fruit']
    print('')

    y.shared = ['candy']
    print(x.shared, x.perobj)  # ['bacon'] ['eggs']
    print(y.shared, y.perobj)  # ['candy'] []
    print(C.shared)  # ['fruit']
