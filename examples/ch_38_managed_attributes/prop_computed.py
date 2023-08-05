# usage: python3 prop_computed.py

class PropSquare:
    # constructor builds a PropSquare object with its value attribute
    # initialized to start
    def __init__(self, start):
        self.value = start

    # return the square of this PropSquare' value attribute
    def getX(self):
        return self.value ** 2  # On attr fetch

    # sets this PropSquare's value attribute to value
    def setX(self, value):
        self.value = value  # On attr assign

    # access and assignment operations on X will be handled by getX() and
    # setX(), respectively
    X = property(getX, setX)  # No delete or docs


if __name__ == '__main__':
    print('code snippets from page 1266\n')

    P = PropSquare(3)
    Q = PropSquare(32)

    print(P.X)  # 9... same as PropSquare.getX(P)... computes X^2 => 9
    print('')
    
    P.X = 4  # setX()
    print(P.X)  # 16... same as PropSquare.setX(P, 4)
    print('')

    print(Q.X)  # 1024... PropSquare.getX(P) computes 32^2
    print('')
