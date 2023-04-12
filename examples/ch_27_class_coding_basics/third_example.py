from second_example import SecondClass


# ThirdClass inherits from SecondClass, which inherits from FirstClass
class ThirdClass(SecondClass):
    # NOTE: the __init__() method runs when a new object is created
    def __init__(self, value):
        self.data = value

    # NOTE: the __add__() method runs with an object of this class appears
    # in an expression using "+"
    def __add__(self, other):
        return ThirdClass(self.data + other)

    # NOTE: the __str__() method runs when an object is printed (converted to
    # its print string by str())
    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):
        self.data *= other  # in-place change


if __name__ == '__main__':
    a = ThirdClass('abc')  # build a ThirdClass object
    a.display()  # Current value = abc... calls SecondClass's display() method
    print(a)  # [ThirdClass: abc]... invokes __str__()

    b = a + 'xyz'  # [ThirdClass: abcxyz]... invokes __add__()
    print(b)

    a.mul(3)  # in-place change
    print(a)  # [ThirdClass: abcabcabc]
