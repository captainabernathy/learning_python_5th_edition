# NOTE: add ns2/dir1 and ns2/dir2 to PYTHONPATH

# usage: python3 ns2.py

if __name__ == '__main__':
    print('code snippets from page 764\n')
   
    # requires that the directories containing sub be on PYTHONPATH
    import sub.mod2  # ns2/dir2/sub/mod2
    import sub.pkg  # ns2/dir1/sub/pkg/__init__.py
    import sub.lower.mod3  # ns2/dir2/sub/lower/mod3
    print('')

    print(sub)  # <module 'sub' (<_frozen...>)>
    print('')

    print(sub.mod2)  # <module 'sub.mod2' from '/path/to/sub/mod2.py'>
    print('')

    print(sub.pkg)  # <module 'sub.pkg' from '/path/to/sub/pkg/__init__.py'>
    print('')
    
    print(sub.lower)  # <module 'sublower' (<_frozen...>)>
    print('')

    # <module 'sub.lower.mod3' from '/path/to/sub/lower/mod3.py'>
    print(sub.lower.mod3)
