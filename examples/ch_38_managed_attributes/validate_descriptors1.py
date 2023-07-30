# NOTE: descriptors are similar to properties EXCEPT that descriptors also
# have their own state

# NOTE: storing state in the descriptor instance instead of the owner (client)
# class instance means that the state will be the same in all owner class
# instances... Descriptor state can vary only once per attribute appearance

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
        # returns this Name's name attribute
        def __get__(self, instance, owner):
            return self.name

        # formats value and sets this Name's name attribute to the result
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value
    # assigns Name descriptor to name attribute
    name = Name()

    # descriptor class for Age attribute
    class Age(object):
        # returns this Age's age attribute
        def __get__(self, instance, owner):
            return self.age  # use descriptor data

        # sets this Age's age attribute to value if it is valid... raises a
        # ValueError if value is invalid
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value
    # assigns Age descriptor to age attribute
    age = Age()

    # descriptor class for Acct
    class Acct(object):
        # returns a formatted version this Acct's acct attribute
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'

        # formats value and sets this Acct's acct attribute to the result if it
        # is valid... raises a TypeError if value is invalid
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:  # use instance class data
                raise TypeError('invalid acct number')
            else:
                self.acct = value
    # assgins Acct descriptor to acct attribute
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
