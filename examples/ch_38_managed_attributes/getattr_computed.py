class AttrSquare:
    # constructor builds an AttrSquare with its value attribute initialized to
    # start
    def __init__(self, start):
        self.value = start

    # returns the square of this AttrSquare's value attribute on accesses to
    # this AttrSquare's X attribute (ie: obj.X)... raises an AttributeError
    # otherwise
    def __getattr__(self, attr):
        '''
        called on undefined attr fetch
        '''
        if attr == 'X':  # compute if value is not undefined
            return self.value ** 2
        else:
            raise AttributeError(attr)

    # sets this AttrSquare's value attribute to value on assignments to this
    # object's X attribute (ie: obj.X = value)
    def __setattr__(self, attr, value):
        '''
        called on all attr assignments
        '''
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value


if __name__ == '__main__':
    print('code snippets from pages 1286\n')

    A = AttrSquare(3)
    B = AttrSquare(32)

    print(A.X)  # 9... same as AttrSquare.__getattr__(A, 'X')
    print('')

    A.X = 4  # same as AttrSquare.__setattr__(A, 'X', 4)
    print(A.X)  # 16... same as AttrSquare.__getattr__(A, 'X')
    print('')

    print(B.X)  # 1024... same as AttrSquare.__getattr__(B, 'X')
    print('')
