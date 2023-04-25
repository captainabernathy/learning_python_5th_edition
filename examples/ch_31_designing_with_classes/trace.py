class Wrapper:
    # constructor initializes this Wrapper's wrapped attribute to object
    def __init__(self, object):
        self.wrapped = object

    # returns the result of calling attrname on this Wrapper's wrapped
    # attribute
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)  # trace fetch
        return getattr(self.wrapped, attrname)  # delegate fetch
