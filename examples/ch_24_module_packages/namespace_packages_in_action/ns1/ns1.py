# NOTE: add ns1/dir1 and ns1/dir2 to PYTHONPATH

# usage: python3 ns1.py

if __name__ == '__main__':
    print('code snippets from page 762\n')

    # requires that the directories containing sub be on PYTHONPATH
    import sub
    print(sub)  # <module 'sub' (<_frozen...>)>
    print('')

    # _NamespacePath(['/path/to/ns1/dir1/sub'], ['/path/to/ns1/dir2/sub'])
    print(sub.__path__)
    print('')

    from sub import mod1  # ns1/dir1/sub/mod1.py
    from sub import mod2  # ns1/dir2/sub/mod2.py
    print('')

    print(mod1)  # <moudle 'sub.mod1' from '/path/to/mod1.py'>
    print('')

    print(sub.mod2)  # <module 'sub.mod2' from '/path/to/sub/mod2.py'>
    print('')

    print(sub)  # <module 'sub' (<_frozen...>)>
