# usage: python3 namespace_dictionaries.py

import module2

if __name__ == '__main__':
    print('code snippets from pages 720-721\n')

    # NOTE: we can access a module's namespace dictionary through its __dict__
    # attribute
    print(list(module2.__dict__.keys()))
    print('')

    # names assigned by only by module
    print(list(name for name in module2.__dict__.keys()
               if not name.startswith('__')))
    print('')

    # same as ^^^
    print(list(name for name in module2.__dict__ if not name.startswith('__')))
    print('')

    # access module2.name directly or by using 'name' as a key to its __dict__
    # attribute
    print(module2.name, module2.__dict__['name'])
