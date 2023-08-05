# usage: python3 getattr2.py

class Wrapper:
    # constructor builds a Wrapper with its wrapped attribute initialized to
    # object
    def __init__(self, object):
        self.wrapped = object

    # returns the result of looking up attrname on this Wrapper's wrapped
    # attribute
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)  # trace lookup
        return getattr(self.wrapped, attrname)  # delegate lookup (to wrapped)


if __name__ == '__main__':
    print('code snippets from page 1282\n')

    X = Wrapper([1, 2, 3])
    
    X.append(4)  # Trace: append... same as Wrapper.__getattr__(X, 'append')(4)
    print('')

    print(X.wrapped)  # [1, 2, 3, 4]...
                      # same as Wrapper.__getattr__(X, '__repr__')()
    print('')
