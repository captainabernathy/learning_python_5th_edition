# usage: python3 comparisons_lt_gt_and_others.py

# NOTE: __gt__() and __lt__() provide > and <, respectively

class C:
    data = 'spam'

    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other


if __name__ == '__main__':
    print('code snippets from page 955\n')

    X = C()
    print(X > 'ham')  # True
    print(X < 'ham')  # False
