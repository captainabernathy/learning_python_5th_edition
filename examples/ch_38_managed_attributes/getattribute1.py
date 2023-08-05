# usage: python3 getattribute1.py

class Catcher(object):  # object needed in 2.X
    # NOTE: __getattribute__() run for all attribute lookups
    def __getattribute__(self, name):
        print('Get: %s' % name)

    # NOTE: __setattr__() is available on all versions of python
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))


if __name__ == '__main__':
    X = Catcher()
    X.job  # Get: job... same as Catcher.__getattribute__(X, 'job')
    print('')

    X.pay  # Get: pay... same as Catcher.__getattribute__(X, 'pay')
    print('')

    X.pay = 99  # Set: pay 99... same as Catcher.__setattr__(X, 'pay', 99)
    print('')
