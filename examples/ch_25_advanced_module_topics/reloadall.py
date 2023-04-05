'''
script transitively reloads nested modules (2.X + 3.X)
'''
# NOTE: you cannot depend on reloads to pick up changes in all the modules in
# a program ransitively as subcomponents must be reloaded independently... this
# module provides a tool for automating this process
import types
from importlib import reload


# outputs a status module
def status(module):
    print('reloading ' + module.__name__)


# attempts to reload the module passed to module... outputs failure
# notification if unsuccessful
def tryreload(module):
    try:
        reload(module)
    except Exception:
        print('FAILED: %s' % module)


# attempts to reload the module passed to module if it is not a key in the
# dictionary passed to visited and recursively attempts to load of the module's
# module attributes
def transitive_reload(module, visited):
    if module not in visited:
        status(module)  # output status update
        tryreload(module)  # attempt to reload module
        visited[module] = True  # update module's status in visited
        # loop over module's attributes
        for attrobj in module.__dict__.values():
            # if type(attrobj) == types.ModuleType:
            # test if current attribute is a module, and if so, recur
            if isinstance(attrobj, types.ModuleType):
                transitive_reload(attrobj, visited)


# automatically reloads a module, every module that the module imports... all
# the way to the bottom of each import chain
def reload_all(*args):
    visited = {}  # starts empty... collect results in dictionary
    # loop over all arguments, and if any is a module, attempt to reload it
    for arg in args:
        # if type(arg) == types.ModuleType:
        if isinstance(arg, types.ModuleType):
            transitive_reload(arg, visited)


# uses the function passed to reloader to reload the module passed to modname
def tester(reloader, modname):
    import importlib
    import sys
    # if there command line arguments
    if len(sys.argv) > 1:
        modname = sys.argv[1]  # use the first one as the module name
    # NOTE: importlib.import_module() returns the module named by its argument
    module = importlib.import_module(modname)  # import module
    reloader(module)  # now reload the module


if __name__ == '__main__':
    print('code snippets from pages 788-791\n')
    tester(reload_all, 'reloadall')
