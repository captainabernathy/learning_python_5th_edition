# usage: python3 index_iteration_getitem.py

# NOTE: Any class that supports for loops automatically supports all iteration
# contexts
class StepperIndex:
    # NOTE: when more specific iteration methods aren't availble __getitem__()
    # serves as a fallback
    def __getitem__(self, i):
        return self.data[i]


if __name__ == '__main__':
    print('code snippets from page 923\n')

    X = StepperIndex()
    X.data = 'Spam'
    print(X[1])  # p

    # for loops call __getitem__()
    for item in X:
        print(item, end=' ')  # S p a m
    print('\n')

    print('p' in X)  # True... in and all call __getitem__() too
    print([c for c in X])  # ['S','p','a','m']... list comprehension

    # map calls __getitem__() (use list() in 3X)
    print(list(map(str.upper, X)))  # ['S','P','A','M']
    print('')

    (a, b, c, d) = X  # sequence assignments use __getitem__()
    print(a, c, d)  # S a m
    print('')

    # ['S','p','a','m'] ('S','p','a','m') Spam
    print(list(X), tuple(X), ''.join(X))
