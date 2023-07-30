class Powers:
    # constructor builds a Powers with its _square and _cube attributes
    # initialized to square and cube respectively
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    # returns the square of this Powers's _square attribute on accesses to this
    # Powers's square attribute (ie: obj.square), OR returns the cube of this
    # Powers's _cube attribute on accesses to this Powers's cube attribute
    # (ie: obj.cube)... raises a TypeError otherwise
    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            return TypeError('unknown attr: ' + name)

    # sets this Powers's _square attribute to value on assignments to this
    # Powers's square attribute (ie: obj.square = value)
    def __setattr__(self, name, value):
        if name == 'square':
            # self.__dict__['_square'] = value  # alternatively, use object
            # alternatively
            object.__setattr__(self, '_square', value)
        else:
            self.__dict__[name] = value


if __name__ == '__main__':
    print('code snippets from pages 1289-1290\n')

    X = Powers(3, 4)
    
    print(X.square)  # 9... same as Powers.__getattr__(X, 'square')
    print('')

    print(X.cube)  # 64... same as Powers.__getattr__(X, 'cube')
    print('')

    X.square = 5  # Powers.__setattr__(X, 'square', 5)
    print(X.square)  # 25... same as Powers.__getattr__(X, 'square')
    print('')
