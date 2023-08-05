# usage: python3 reloadall3.py

'''
script transitively reloads nested modules using an explicit stack with a
generator expression
'''
import types
from reloadall import status
from reloadall import tryreload
from reloadall import tester


# attempts to reload any module in the list passed to modules that are not
# accounted for in the set passed to visited... any dependent submodules of
# any module are loaded recursively via a generator expression
def transitive_reload(modules, visited):
    while modules:
        next_mod = modules.pop()
        status(next_mod)
        tryreload(next_mod)
        visited.add(next_mod)
        modules.extend(x for x in next_mod.__dict__.values()
                       # if type(x) == types.ModuleType and x not in visited)
                       if isinstance(x, types.ModuleType) and x not in visited)


# attempts to reload any number of potential modules packed into the modules
# argument
def reload_all(*modules):
    transitive_reload(list(modules), set())


if __name__ == '__main__':
    print('code snippets from pages 792-793\n')

    tester(reload_all, 'reloadall3')
