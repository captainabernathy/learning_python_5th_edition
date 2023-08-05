# usage: python3 getattribute_computed.py

class AttrSquare(object):
    # construct builds an AttrSquare with its value attribute initialized to
    # start
    def __init__(self, start):
        self.value = start

    # returns the square of this AttrSquare's value attribute on accesses to
    # this AttrSquare's X attribute (ie: obj.X)
    def __getattribute__(self, attr):
        '''
        called on all attr fetches...
        avoid looping by using direct superclass method calls instead of
        __dict__ keys
        '''
        if attr == 'X':
            # return self.value ** 2  # triggers __getattribute__ again!
            # more efficiently...
            return object.__getattribute__(self, 'value') ** 2
        else:
            return object.__getattribute__(self, attr)  # avoid looping

    # sets this AttrSquare's value attribute to value on assignments to this
    # AttrSquare's X attribute (obj.X = value)
    def __setattr__(self, attr, value):
        '''
        called on all attr assignments
        '''
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)


if __name__ == '__main__':
    print('code snippets from pages 1286-1287\n')

    A = AttrSquare(3)
    B = AttrSquare(32)

    print(A.X)  # 9... same as AttrSquare.__getattribute__(A, 'X')
    print('')

    A.X = 4  # same as AttrSquare.__setattr__(A, 'X', 4)
    print(A.X)  # 16... same as AttrSquare.__getattribute__(A, 'X')
    print('')

    print(B.X)  # 1024... same as AttrSquare.__getattribute__(B, 'X')
    print('')
