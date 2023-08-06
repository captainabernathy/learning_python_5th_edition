# usage: python3 metaclass_05_02.py

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call:', classname)
        return type.__call__(meta, classname, supers, classdict)


class SubMeta(SuperMeta):
    def __init__(Class, classname, supers, classdict):
        print('In SubMeta.init:', classname)


if __name__ == '__main__':
    print('code snippets from pages 1424-1425\n')

    print(SubMeta.__class__)  # <class 'type'>
    print('')

    # ['SubMeta', 'SuperMeta', 'type', 'object']
    print([n.__name__ for n in SubMeta.__mro__])
    print('')

    print(SubMeta.__call__)  # <function SuperMeta.__call__ at 0x...>
    print('')

    # NOTE: explicit instantiation invokes a super class's __call__() method
    # In SuperMeta.call: xxx
    # In SubMeta.init: xxx
    SubMeta.__call__(SubMeta, 'xxx', (), {})
    print('')

    # NOTE: HOWEVER... normal, built-in calls to a constructor DO NOT invoke a
    # super class's __call__() method
    SubMeta('yyy', (), {})  # In SubMeta.init: yyy

