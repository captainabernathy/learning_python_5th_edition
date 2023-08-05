# usage: python3 descriptors_the_basics.py

# NOTE: the __delete__() method is called on attempts to delete a managed
# attribute (similar to __delattr__), while the __del__() method is the
# general instance destructor method, which is run when an instance of any kind
# is about to get garbage collected

# NOTE: a descriptor class refers to a class that provides special methods such
# as __get__(), __set__(), and __delete__() that are automatically run when
# a corresponding action is performend on a specified attribute
class Descriptor:  # Add (object) in 2.X
    # NOTE: the __get__() method receives the descriptor class instance (self),
    # the instance of the client class that the descriptor instance is attached
    # to (instance), and the class to which the descriptor instance is attached
    # (owner)
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')


class Subject:
    # access to attr handled by Descriptor's __get__()
    attr = Descriptor()  # assigns Descriptor() instance to attr


class D1:
    def __get__(*args):
        print('get')


class C1:
    # access to a handled by D1's __get__()
    a = D1()


class D2:
    def __get__(*args):
        print('get')

    def __set__(*args):  # makes descriptor-based attribute read-only
        raise AttributeError('cannot set')


class C2:
    a = D2()


if __name__ == '__main__':
    print('code snippets from pages 1270-1271\n')

    X = Subject()
    # <__main__.Descriptor object at 0x...> => self
    # <__main__.Subject object at 0x...> => instance
    # <class '__main__.Subject'> => owner
    X.attr
    print('')

    # <__main__.Descriptor object at 0x...> => self
    # None => instance
    # <class'__main__.Subject'>  => owner
    Subject.attr
    print('')

    X = C1()
    X.a  # get... runs inherited descriptor __get__()
    print('')

    C1.a  # get... __get__()
    print('')

    X.a = 99  # Stored on X... hides C1.a
    print(X.a)  # 99
    print('')

    print(list(X.__dict__.keys()))  # ['a']
    print('')

    Y = C1()  # inherits descriptor
    Y.a  # get... __get__()
    print('')

    C1.a  # get... __get__()
    print('')

    X = C2()
    X.a  # get... __get__()
    print('')

    try:
        X.a = 99  # error... a is read only!
    except AttributeError as ex:
        print(ex)  # cannot set
    print('')
