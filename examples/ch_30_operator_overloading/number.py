# usage: python3 number.py

# class meant to represent a number
class Number:
    # constructor initializes this Number's data to start
    def __init__(self, start):
        self.data = start

    # subtraction operator... subtracts other from this Number's data and
    # returns the result
    def __sub__(self, other):
        return Number(self.data - other)  # returns a new instance


if __name__ == '__main__':
    print('code snippets from page 917\n')

    X = Number(5)
    Y = X - 2  # X.data - 2
    print(Y.data)  # 3
