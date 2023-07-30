# NOTE: Becase every attribute fetch is routed to __getattribute__(), there is
# no need to mangle names to intercept them... OTHO, it is necessary to route
# nonmanged attribute fetches to a superclass to avoid looping or extra calls

class CardHolder(object):
    # class attributes
    acctlen = 8
    retireage = 59.5

    # constructor builds a CardHolder with its acct, name, age, and addr
    # attributes initialized to acct, name, age, and addr respectively
    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr  # not managed

    # runs on all attribute accesses...
    # on accesses to...
    #   a) obj.acct -> returns a formatted version of this CardHolder's acct
    #      attribute (through object)
    #   b) obj.remain -> returns the number of years remaining until this
    #      CardHolder's retirement age (through object)
    def __getattribute__(self, name):
        superget = object.__getattribute__  # loop one level up on attr fetches
        if name == 'acct':
            return superget(self, 'acct')[:-3] + '***'
        elif name == 'remain':
            return superget(self, 'retireage') - superget(self, 'age')
        else:
            return superget(self, name)

    # runs on all attr assignments, addr gets stored directly
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
        if name == 'name':
            value = value.lower().replace(' ', '_')
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value
