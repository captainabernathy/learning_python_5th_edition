# NOTE: Properties run code automatically on attribute access, but they cannot
# be used to intercept all attributes generically

class CardHolder(object):
    # class attributes
    acctlen = 8
    retireage = 59.5

    # constructor builds a CardHolder with its acct, name, age, and addr
    # attributes initialized to acct, name, age, and addr respectively
    def __init__(self, acct, name, age, addr):
        self.acct = acct  # invokes set_name
        self.name = name  # invokes set_name
        self.age = age  # invokes set_name
        self.addr = addr  # not managed... can be accessed directly

    # returns this CardHolder's _name attribute
    def get_name(self):
        return self._name

    # sets this CardHolder's _name attribute to the string value after
    # transforming it to lowercase and replacing spaces with underscores
    def set_name(self, value):
        value = value.lower().replace(' ', '_')
        self._name = value

    # accesses and assignements to this CardHolder's name attribute will be
    # handled by this CardHolder's get_name() and set_name() methods
    name = property(get_name, set_name)

    # returns this CardHolder's _age attribute
    def get_age(self):
        return self._age

    # sets this CardHolder's _age attribute to value provided that value is
    # between 0 and 150... raises a ValueError otherwise
    def set_age(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self._age = value

    # accesses and assignments to this CardHolder's age attribute will be
    # handled by this CardHolder's get_age() and set_age() methods
    age = property(get_age, set_age)

    # returns a representation of this CardHolder's _acct attribute
    def get_acct(self):
        return self._acct[:-3] + '***'

    # sets this CardHolder's _acct attribte to a representation of value,
    # provided it is valid... raises TypeError otherwise
    def set_acct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invalid acct number')
        else:
            self._acct = value

    # accesses and assignments to this CardHolder's acct attribute will be
    # handled by this CardHolder's get_acct() and set_acct() methods
    acct = property(get_acct, set_acct)

    # returns the number of years remaining until this CardHolder's retirement
    # age
    def remain_get(self):
        return self.retireage - self.age

    # accesses to this CardHolder's remain attribute will be handled by this
    # CardHolder's remain_get() method
    remain = property(remain_get)  # read only attribute
