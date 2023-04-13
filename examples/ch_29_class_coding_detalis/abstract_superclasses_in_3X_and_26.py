from abc import ABCMeta
from abc import abstractmethod


# NOTE: in python 3X use a keyword argument in the class header along with the
# @ decorator syntax inside of the class to indicate that a class is an
# abstract base class
class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()  # expects action to be defined by a subclass

    # NOTE: a class with an abstract method cannot be instantiated unless all
    # of its abstract methods have been defined in subclasses
    @abstractmethod
    def action(self):  # must be implemented by subclasses
        pass


class Sub(Super):
    def action(self):  # implements action
        print('spam')


if __name__ == '__main__':
    print('code snippets from pages 899-900\n')
    try:
        X = Super()
    except TypeError as err:
        # TypeError: Can't instantiate abstract class Super with abstract
        # method action
        print('TypeError:', err)

    X = Sub()
    X.delegate()  # spam
