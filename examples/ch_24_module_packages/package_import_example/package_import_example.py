# usage: python3 package_import_example.py

# no need to update PYTHONPATH
# NOTE: import statements run each directory's initialization file the first
# time that directory is traversed
import dir1.dir2.mod

# NOTE: modules and directories can be passed to reload() to force re-execution
# of that item
from importlib import reload

if __name__ == '__main__':
    print('\ncode snippets from pages 736-737\n')

    reload(dir1)  # dir1 init
    print('')

    reload(dir1.dir2)  # dir2 init
    print('')

    # NOTE: once imported, the path in your import statement becomes a nested
    # object path in your script... each directory name in the path becomes a
    # variable assigned to a module object whose namesapce is initialized by
    # all the assignments in that directory's __init__.py

    # <module 'dir1' 'pwd/dir1/__init__.py'>
    print(dir1)
    print('')

    # <module 'dir1.dir2' 'pwd/dir1/dir2/__init__.py'>
    print(dir1.dir2)
    print('')

    # <module 'dir1.dir2.mod' 'pwd/dir1/dir2/mod.py'>
    print(dir1.dir2.mod)
    print('')

    print(dir1.x)  # 1... x initialized in dir1's __init__.py
    print(dir1.dir2.y)  # 2... initialized in dir2's __init__.py
    print(dir1.dir2.mod.z)  # 3... initialized ind dir2's mod module
