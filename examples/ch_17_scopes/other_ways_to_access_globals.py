# usage: python3 other_ways_to_access_globals.py

import thismod

if __name__ == '__main__':
    print('code snippets from pages 519-520\n')

    print(thismod.var)  # output thismod's global variable var
    print('')

    thismod.test()  # update thismod's global variable var
    print('')

    print(thismod.var)  # ouput update to this mod's global variable var
