# NOTE: instance methods can be called by a class or an object of a class...
# however when an instance method is called by a class directly, it must be
# passed an object of the class, but when it is called by an object, it is
# implicitly passed a self instance
#
# static methods can be called by a class or an object of a class, and neither
# require nor implicitly receive a self instance or a class reference when
# called
#
# class methods can be called by a class or an object of a class... however in
# both cases the method is implicitly passed a reference to the class when
# called

class Methods:
    '''
    unifies 2X and 3X printing with lists
    '''
    def imeth(self, x):
        print(self, x)  # normal instance method... passed a self

    def smeth(x):
        print([x])  # static... no instance passed

    def cmeth(cls, x):
        print([cls, x])  # gets a class not instance

    # these final assignments ovewrite the assignments made by the defs above
    # and make smeth() and cmeth() static and class methods, respectively
    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)
