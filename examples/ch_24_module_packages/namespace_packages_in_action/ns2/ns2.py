# NOTE: add ns2/dir1 and ns2/dir2 to PYTHONPATH

# usage: python3 ns2.py

if __name__ == '__main__':
    print('code snippets from pages 762-763\n')

    # requires that the directories containing sub be on PYTHONPATH
    import sub.mod1  # ns2/dir1/sub/mod1.py
    import sub.mod2  # ns2/dir2/sub/mod2.py
    print('')

    print(sub.mod1)  # <module 'sub.mod1' from '/path/to/sub/mod1.py'>
    print('')

    print(sub.mod2)  # <module 'sub.mod2' from '/path/to/sub/mod2.py'>>
    print('')

    print(sub)  # <module 'sub' (<_frozen...>)>
    print('')

    # _NamespacePath(['/path/to/ns2/dir1/sub'], ['/path/to/ns2/dir2/sub'])
    print(sub.__path__)

