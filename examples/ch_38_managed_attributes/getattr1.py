# usage: python3 getattr1.py

class Catcher:
    # NOTE: __getattr__() is run for undefined attribute lookups bc it is only
    # run for attributes not stored on an instance or inherited from one of its
    # classes
    def __getattr__(self, name):
        print('Get: %s' % name)

    # NOTE: __setattr__() and __getattr__() are available on all versions of
    # python
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))


if __name__ == '__main__':
    print('code snippets from page 1281\n')

    X = Catcher()
    X.job  # Get: job... same as Catcher.__getattr__(X, 'job')
    print('')

    X.pay  # Get: pay... same as Catcher.__getattr__(X, 'job')
    print('')

    X.pay = 99  # Set: pay 99... same as Catcher.__setattr__(X, 'pay', 99)
    print('')
