# usage: python3 function_annotations_in_3x.py

def func1(a, b, c):
    return a + b + c


# NOTE: function annotations are coded in function headers as arbitrary
# expressions associated with arguments and return values...
# for arguments, aggnotations appear after a colon follow an argument...
# for return values, annotations appear following a -> between the closing
# parentheses and the colon at the end of the function header
def func2(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c


def func3(a: 'spam', b, c: 99):
    return a + b + c


# NOTE: to use default arguments for functions with annotations, assign the
# default after the annotation
# give attributes default values
def func4(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c


def func5(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c


if __name__ == '__main__':
    print('code snippets from pages 588-589\n')

    print(func1(1, 2, 3))  # 6
    print('')

    # NOTE: calls to annotated functions work as usual, but when annotations
    # are present, python collects them in a dictionary and attaches them
    # to the function object
    print(func2(1, 2, 3))  # 6
    # {'a':'spam', 'b':(1,10), 'c':<class 'float'>, 'return': <class 'int'>}
    print(func2.__annotations__)
    print('')

    print(func3(1, 2, 3))  # 6
    print(func3.__annotations__)  # {'a':'spam', 'c':99}
    print('')

    for arg in func3.__annotations__:
        print(arg, '=>', func3.__annotations__[arg])  # a=>spam, c=>99
    print('')

    print(func4(1, 2, 3))  # 6
    print(func4())  # 15... uses defaults
    print(func4(1, c=10))  # 16... pass a by position, override c by name,
                           # use default for b

    # {'a':'spam', 'b':(1,10), 'c':<class 'float'>, 'return': <class 'int'>}
    print(func4.__annotations__)
    print('')

    print(func5(1, 2))  # 9
    print(func5.__annotations__)
