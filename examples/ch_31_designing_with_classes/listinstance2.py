class ListInstance:
    '''
    Mixin class that provides a formatted print() or str() of instances via
    inheritance of __str__... displays instance attrs only... self is instance
    of lowest class... __X names avoid clashing with client's attrs
    '''
    def __attrnames(self):
        # result = ''  # start empty
        # # loop over this ListInstance's attributes
        # for attr in sorted(self.__dict__):
        #     # format each as attr=value
        #     result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        # return result
        # More simply... 
        return ''.join('\t%s=%s\n' % (attr, self.__dict__[attr])
                       for attr in sorted(self.__dict__))

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (self.__class__.__name__,
                                                      id(self),
                                                      self.__attrnames())


if __name__ == '__main__':
    print('code snippets from page 991\n')

    import testmixin
    testmixin.tester(ListInstance)
