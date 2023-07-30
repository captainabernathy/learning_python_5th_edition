class Powers(object):  # for 2.X compatibility
    '''
    manages 2 dynamically computed attributes with properties
    '''
    # NOTE: base values are stored in names that begin with an underscore so
    # that they don't clash with the names of the properties themselves

    # constructor builds a Powers with its _square attribute initialized to
    # square and its _cube attribute initialized to cube
    def __init__(self, square, cube):
        self._square = square  # _square is base value, square is property
        self._cube = cube  # _cube is base value, cube is property

    # returns the square of this Powers's _square attribute
    def get_square(self):
        return self._square ** 2

    # sets the value of this Powers's _square attribute to value
    def set_square(self, value):
        self._square = value

    # accesses and assignments to this Powers's _square attribute will be
    # handled by get_square() and set_square(), respectively
    square = property(get_square, set_square)

    # returns the cube of this Powers's _cube attribute
    def get_cube(self):
        return self._cube ** 3

    # accesses to this Powers's _cube attribute will be handled by get_cube()
    cube = property(get_cube)


if __name__ == '__main__':
    print('code snippets from pages 1288-1289\n')

    X = Powers(3, 4)
    print(X.square)  # 9... same as Powers.get_square(X)
    print('')

    print(X.cube)  # 64... same as Powers.get_cube(X)
    print('')

    X.square = 5  # same as Powers.set_square(X, 5)

    print(X.square)  # 25... same as Powers.get_square(X)
    print('')
