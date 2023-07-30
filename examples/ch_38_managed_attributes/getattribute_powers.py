class Powers(object):
    # constructor builds a Powers with its _square and _cube attributes
    # initialized to square and cube respectively
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    # returns the square of this Powers's _square attribute on accesses to this
    # Powers's square attribute (ie: obj.square), OR returns the cube of this
    # Powers's _cube attribute on accesses to this Powers's cube attribute
    # (ie: obj.cube)
    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name)

    # sets this Powers's _square attribute to value on assignments to this
    # Powers's square attribute (ie: obj.square = value)
    def __setattr__(self, name, value):
        if name == 'square':
            object.__setattr__(self, '_square', value)
        else:
            object.__setattr__(self, name, value)


if __name__ == '__main__':
    print('code snippets from page 1290\n')

    X = Powers(3, 4)
    print(X.square)  # 9... same as Powers.__getattribute__(X, 'square')
    print('')

    print(X.cube)  # 16... same as Powers.__getattribute__(X, 'cube')
    print('')

    X.square = 5  # same as... Powers.__setattr__(X, 'square', 5)
    print(X.square)  # 25... same as Powers.__getattribute__(X, 'square')
    print('')
