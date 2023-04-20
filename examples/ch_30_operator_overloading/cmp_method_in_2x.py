from __future__ import print_function


class C:
    data = 'spam'

    # NOTE: in python 2.X ONLY __cmp__() is a fallback if more specific methods
    # are not dont defined
    def __cmp__(self, other):  # 2X only
        return cmp(self.data, other)


if __name__ == '__main__':
    print('code snippets from pages 955-956\n')
    X = C()
    print(X > 'ham')  # True
    print(X < 'ham')  # False
