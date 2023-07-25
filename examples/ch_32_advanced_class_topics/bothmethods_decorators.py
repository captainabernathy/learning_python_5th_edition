class Methods(object):  # 2.X for properties
    # instance method... first argument is an instance
    def imeth(self, x):
        print([self, x])

    # static method... does not receive an instance
    @staticmethod
    def smeth(x):
        print([x])

    # class method... first argument is a class
    @classmethod
    def cmeth(cls, x):
        print([cls, x])

    # property... first argument is an instance... called implicitly on
    # attribute access to name. ie: obj.name
    @property
    def name(self):
        return 'Bob ' + self.__class__.__name__
