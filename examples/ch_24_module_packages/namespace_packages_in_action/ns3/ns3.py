# NOTE: add ns3/dir1 and ns3/dir2 to PYTHONPATH

# usage: python3 ns3.py

if __name__ == '__main__':
    print('code snippets from page 763\n')

    # requires that the directories containing sub be on PYTHONPATH
    import sub.mod1  # ns3/dir1/sub/mod1.py
    import sub.mod2  # ns3/dir2/sub/mod2.py
    print('')

    print(sub.mod1)  # <module 'sub.mod1' from '/path/to/sub/mod1.py'>
    print('')

    print(sub.mod2)  # <module 'sub.mod2' from '/path/to/sub/mod2.py'>
    print('')

    print(sub)  # <module 'sub' (<_frozen...>)>
    print('')

    # _NamespacePath(['/path/to/ns3/dir1/sub'], ['/path/to/ns3/dir2/sub'])
    print(sub.__path__)

