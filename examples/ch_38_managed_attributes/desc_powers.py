class DescSquare(object):
    # returns the square of instance's _square attribute
    def __get__(self, instance, owner):
        return instance._square ** 2

    # sets instance's _square attribute to value
    def __set__(self, instance, value):
        instance._square = value


class DescCube(object):
    # returns the cube of instance's _cube attribute
    def __get__(self, instance, owner):
        return instance._cube ** 3


class Powers(object):
    square = DescSquare()  # assign descriptor DescSquare to square attribute
    cube = DescCube()  # assign descriptor DescCube to cube attribute

    # NOTE: underscores needed so as to not clash with the names of the
    # descriptors

    # constructor builds a Powers with its _square and _cube attributes
    # initialized to square and cube respectively
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube


if __name__ == '__main__':
    print('code snippets from page 1289\n')

    X = Powers(3, 4)
    print(X.square)  # 9
    print('')

    print(X.cube)  # 64
    print('')

    X.square = 5
    print(X.square)  # 25
    print('')
