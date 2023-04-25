class ListInherited:
    '''
    Use dir() to collect both instance attrs and names inherited from its
    classes... 3.x show more names than 2.x due to the implied object
    superclass... getattr() fetches inherited names not in self.__dict__... use
    __str__, NOT __repr__, or else this loops when printing bound methods
    '''
    def __attrnames(self):
        result = ''
        for attr in dir(self):  # instance dir()
            if attr[:2] == '__' and attr[-2:] == '__':  # skip internals
                result += '\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr, getattr(self, attr))
        return result
    
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (self.__class__.__name__,
                                                      id(self),
                                                      self.__attrnames())


if __name__ == '__main__':
    print('code snippets from page 997\n')

    import testmixin
    testmixin.tester(ListInherited)
