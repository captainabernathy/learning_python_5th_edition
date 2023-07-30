# Here, attributes of CardHolder are stored as per-instance data instead of
# descriptor instance data

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

    # descriptor class for name attribute
    class Name(object):
        # returns instance's __name attribute
        def __get__(self, instance, owner):
            return instance.__name

        # formats value and sets instance's __name attribute to the result
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            instance.__name = value
    # assigns Name descriptor to name attribute
    name = Name()

    # descriptor class for Age attribute
    class Age(object):
        # returns instance's __age attribute
        def __get__(self, instance, owner):
            return instance.__age  # use descriptor data

        # sets instance's __age attribute to value if it is valid... raises a
        # ValueError if value is invalid
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                instance.__age = value
    # assigns Age descriptor to age attribute
    age = Age()

    class Acct(object):
        # returns a formatted version of instance's __acct attribute
        def __get__(self, instance, owner):
            return instance.__acct[:-3] + '***'

        # formats value and sets instances __acct attribute to the result if it
        # is valid... raises a TypeError if value is invalid
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:  # use instance class data
                raise TypeError('invalid acct number')
            else:
                instance.__acct = value
    # assigns Acct descriptor to acct attribute
    acct = Acct()

    # descriptor class for Remain
    class Remain(object):
        # returns the number of years remaining until instance's retirement age
        def __get__(self, instance, owner):
            return instance.retireage - instance.age  # calls Age.__get__()

        # raises a TypeError on attempts to assign to remain
        def __set__(self, instance, value):
            raise TypeError('cannot set remain')
    # assigns Remain descriptor to remain attribute
    remain = Remain()
