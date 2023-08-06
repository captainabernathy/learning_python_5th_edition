# usage: python3 class_statement_protocol.py

if __name__ == '__main__':
    print('code snippets from pages 1414-1415\n')

    # NOTE: in 3X and 2X new-style classes
    #   a) type is a class that generates classes
    #   b) metaclasses are subclasses of the type class
    #   c) class objets are instances of the type class (or a subtype thereof)
    #   d) (instance) objects are generated from a class

    # class protocol:
    # class = type(classname, superclass, attributedict)
    x = type('Spam', (), {'data': 1, 'meth': (lambda x, y: x.data + y)})

    i = x()

    print(x)  # <class '__main__.Spam'>
    print('')

    print(i)  # <__main__.Spam object at 0x...>
    print('')

    print(i.data)  # 1
    print('')

    print(i.meth(2))  # 3
    print('')

    print(x.__bases__)  # (<class 'object'>,)
    print('')

    # [('data', 1), ('meth', <function <lambda> at 0x...>)]
    print([(a, v) for (a, v) in x.__dict__.items() if not a.startswith('__')])
