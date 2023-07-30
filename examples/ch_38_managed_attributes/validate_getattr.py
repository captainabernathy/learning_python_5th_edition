class CardHolder:
    # class attributes
    acctlen = 8
    retireage = 59.5

    # constructor builds a CardHolder with its acct, name, age, and addr
    # attributes initialized to acct, name, age, and addr respectively
    def __init__(self, acct, name, age, addr):
        # these assignments trigger __setattr__()
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr  # not managed

    # NOTE: __getattr__() is run on undefined attribute accesses... in this
    # case name, age, and addr are defined while acct and remain are computed

    # runs on accesses to undefined attributes
    # on accesses to:
    #   a) obj.acct -> returns a formatted version of this CardHolder's _acct
    #      attribute
    #   b) obj.remain -> returns the number of years remaining until this
    #      CardHolder's retirement age
    #   c) raises AttributeError otherwise
    def __getattr__(self, name):
        if name == 'acct':
            return self._acct[:-3] + '***'
        elif name == 'remain':
            return self.retireage - self.age  # doesn't trigger __getattr__()
        else:
            raise AttributeError(name)

    # runs on attribute assignments....
    # on assignments to:
    #   a) obj.name -> formats value and sets the result to this CardHolder's
    #      name attribute
    #   b) obj.age -> sets value to this CardHolder's age if it is valid...
    #      raises ValueError if value is invalid
    #   c) obj.acct -> formats value and sets the result to this CardHolder's
    #      _acct attribute if it is valid... raises a TypeError if value is
    #      not valid
    #   d) obj.remain -> raises a TypeError
    def __setattr__(self, name, value):
        if name == 'name':  # stored on instance... ensures future accesses
            value = value.lower().replace(' ', '_')  # don't call __getattr__()
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':  # stored as _acct so that later accesses do call
            name = '_acct'    # __getattr__()
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value  # avoid looping
