# usage: python3 files_still_have_precedence_over_directories.py
if __name__ == '__main__':
    print('code snippets from pages 765-766\n')

    import ns2
    # when PYTHONPATH is empty...
    # or
    # when PYTHONPATH is '/path/to/ns4/dir1:/path/to/ns4/dir2'
    # ^^^ <module 'ns2' (<_frozen...>)>
    # when PYTHONPATH is /path/to/ns3/dir ...
    # <module 'ns2' from '/path/to/ns3/dir/ns2.py'>
    print(ns2)
    print('')

    try:
        # when PYTHONPATH is empty...
        # or
        # when PYTHONPATH is '/path/to/ns4/dir1:/path/to/ns4/dir2'
        # ^^^ _NamespacePath(['/path/to/ns2']) ... a directory
        print(ns2.__path__)
    except AttributeError as ex:
        # when PYTHONPATH is /path/to/ns3/dir ...
        # ^^^ module 'ns2' has no attribute '__path__'
        # bc lookup finds file /ns3/dir/ns2.py on PYTHONPATH
        print(ex)
    print('')

    import sys
    # when PYTHONPATH is empty...
    # ^^^ ['/path/to/cwd','/usr/lib/pythonXX']
    # when PYTHONPATH is /path/to/ns3/dir ...
    # ^^^ ['/path/to/ns3/dir']
    # when PYTHONPATH is '/path/to/ns4/dir1:/path/to/ns4/dir2'
    # ^^^ ['/path/to/ns4/dir1','/path/to/ns4/dir2']
    print(sys.path[:2])
