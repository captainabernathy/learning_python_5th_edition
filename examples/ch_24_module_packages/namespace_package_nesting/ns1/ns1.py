# NOTE: add ns1/dir1 and ns1/dir2 to PYTHONPATH

# usage: python3 ns1.py

if __name__ == '__main__':
    print('code snippets from pages 763-764\n')
    
    # requires that the directories containing sub be on PYTHONPATH
    # namespace package nested in namespace package
    import sub.lower.mod3  # ns1/dir2/sub/lower/mod3
    import sub
    import sub.mod2  # ns1/dir2/sub/mod2
    print('')

    print(sub.lower)  # <module 'sub.lower' (<_frozen...>)>
    print('')

    # _NamespacePath(['/path/to/ns1/dir2/sub/lower'])
    print(sub.lower.__path__)
