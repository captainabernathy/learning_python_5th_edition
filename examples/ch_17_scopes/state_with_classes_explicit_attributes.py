# simple class that provides a function for updating an attribute
class tester1:
    def __init__(self, start):
        self.start = start

    def nested(self, label):
        print(label, self.start)
        self.start += 1


# class that overloads the function call operator in order to provide objects
# of the class with a means to update an attribute
class tester2:
    def __init__(self, start):
        self.start = start

    def __call__(self, label):
        print(label, self.start)
        self.start += 1


if __name__ == '__main__':
    print('code snippets from pages 535-536\n')
    F = tester1(0)
    F.nested('spam')  # spam 0
    F.nested('ham')  # ham 1
    print('')

    G = tester1(42)
    G.nested('toast')  # toast 42
    G.nested('bacon')  # bacon 43
    F.nested('eggs')  # bacon 2
    print('')

    # access start attribute directly
    print(F.start)  # 3
    print(G.start)  # 44
    print('')

    H = tester2(99)
    H('juice')  # juice 99... via overloaded function call operator
    H.__call__('pancakes')  # pancakes 100 call function operator directly
