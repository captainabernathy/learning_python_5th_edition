# usage: python3 reloadall2.py

'''
script transitively reloads nested modules using a set and dictionary object
'''
import types
from reloadall import status
from reloadall import tryreload
from reloadall import tester


# attempts to reload any of the module objects passed to objects that are not
# accounted for in the set passed to visited... any dependent submodules of any
# module are loaded recursively
def transitive_reload(objects, visited):
    # loop over each objects
    for obj in objects:
        # if an object is a module that has not been visited... attempt to
        # reload it and mark it as visited
        # if type(obj) == types.ModuleType and obj not in visited:
        if isinstance(obj, types.ModuleType) and obj not in visited:
            status(obj)  # output status update
            tryreload(obj)  # attempt to reload modlue
            visited.add(obj)  # mark module as visited
            # recur to reload any dependent submodules
            transitive_reload(obj.__dict__.values(), visited)


# attempts to reload any modules contained in args
def reload_all(*args):
    transitive_reload(args, set())


if __name__ == '__main__':
    print('code snippets from pages 788-791\n')

    tester(reload_all, 'reloadall2')
