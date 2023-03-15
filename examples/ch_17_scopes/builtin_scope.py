# NOTE: thie built-in scope is implemented as a standard library module called
# builtins... BUT you have to import builtins in order to access the name
# builtins

import builtins

if __name__ == '__main__':
    print('code snippets from pages 512-513\n')

    print(dir(builtins))  # attributes available within the builtins module
    print('')

    print(zip)  # <class 'zip'>
    print(builtins.zip)  # <class, 'zip'>
    print('')

    # same object... different lookups
    print(zip is builtins.zip)
    print('')

    # total number of attributes vs named attributes available within builtins
    print(len(dir(builtins)), len([x for x in dir(builtins)
          if not x.startswith('__')]))
