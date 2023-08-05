# usage: python3 getattr_vs_getattribute.py

class GetAttr:
    attr1 = 1  # initializes class-level attribute to 1

    # constructor builds a GetAttr with its attr2 attribute initialized to 2
    def __init__(self):
        self.attr2 = 2

    # returns 3 on accesses to this GetAttr's attr3 attribute (ie: obj.attr3)..
    # raises an AttributeError otherwise
    def __getattr__(self, attr):
        '''
        called on undefined attrs only
        '''
        print('getattr: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            raise AttributeError(attr)


class GetAttribute(object):  # object needed in 2.X
    attr1 = 1  # initializes class-level attribute to 1

    # constructor builds a GetAttribute with its attr2 attribute initialized to
    # 22
    def __init__(self):
        self.attr2 = 2

    # returns 3 on accesses to this Getattribute's attr3 attribute
    # (obj.attr3)
    def __getattribute__(self, attr):
        '''
        called on all attr fetches
        '''
        print('getattribute: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)  # avoid looping


if __name__ == '__main__':
    print('code snippets from pages 1287-1288\n')

    X = GetAttr()
    print(X.attr1)  # 1.. direct access to class attribute
    print('')

    print(X.attr2)  # 2... direct access to instance attribute
    print('')

    print(X.attr3)  # 3... same as GetAttr.__getattr__(X, 'attr3')

    print('')
    print('-' * 20)
    print('')

    X = GetAttribute()

    print(X.attr1)  # 1... direct access to class attribute
    print('')

    print(X.attr2)  # 2... direct access to instance attribute
    print('')

    print(X.attr3)  # 3... same as GetAttribute.__getattribute__(X, 'attr3')
