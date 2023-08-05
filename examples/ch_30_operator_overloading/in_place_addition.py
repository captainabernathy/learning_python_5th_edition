# usage: python3 in_place_addition.py

class Number1:
    def __init__(self, val):
        self.val = val

    # NOTE: __iadd__() provides +=
    def __iadd__(self, other):
        self.val += other
        return self


class Number2:
    def __init__(self, val):
        self.val = val

    # __add__() runs as a fall back to __iadd__(), but "may"" not be able to
    # optimize in-place updates
    def __add__(self, other):
        return Number2(self.val + other)


if __name__ == '__main__':
    print('code snippets from page 950\n')

    x = Number1(5)
    print(x.val)  # 5
    x += 1
    print(x.val)  # 6
    x += 1
    print(x.val)  # 7

    y = Number1([1])
    print(y.val)  # [1]
    y += [2]  # += performs list concatenation
    print(y.val)  # [1,2]
    y += [3]
    print(y.val)  # [1,2,3]
    print('')

    x = Number2(5)
    print(x.val)  # 5
    x += 1
    print(x.val)  # 6
    x += 1
    print(x.val)  # 7
    print('')

    y = Number2([1])
    print(y.val)  # [1]
    y += [2]
    print(y.val)  # [1,2]
    y += [3]
    print(y.val)  # [1,2,3]
