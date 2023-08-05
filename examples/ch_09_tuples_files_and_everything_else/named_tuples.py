# usage: python3 named_tuples.py

from collections import namedtuple

if __name__ == '__main__':
    print('code snippets from pages 289-291\n')

    bob = ('Bob', 40.5, ['dev', 'mgr'])
    print(bob)  # ('Bob', 40.5, ['dev', 'mgr'])
    print(bob[0], bob[2])  # Bob ['dev','mgr']
    print('')

    bob = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
    print(bob)
    print(bob['name'], bob['jobs'])  # Bob ['dev','mgr']
    print('')

    # convert elements in dictionary to a tuple
    print(tuple(bob.values()))  # ('Bob',40.5,['dev','mgr'])

    # convert key/value pairs in dictionary to a list of tuples
    # [('name','Bob'),('age',40.5), ('jobs',['dev','mgr'])]
    print(list(bob.items()))
    print('')

    # NOTE: the namedtuple() extension adds logic to tuples that allows
    # components to be accessed by position and attribute name

    # a namedtuple provides a generalized template for creating a class from
    # which objects can be generated

    # the Rec class contains name, age, and jobs fields
    Rec = namedtuple('Rec', ['name', 'age', 'jobs'])  # a generalized class
    
    # create an object from a Rec
    bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])  # a namedtuple record

    # Rec(name='Bob',age=40.5,jobs=['dev','mgr'])
    print(bob)
    print(bob[0], bob[2])  # access by position... Bob ['dev','mgr']
    print(bob.name, bob.jobs)  # access by attribute... Bob ['dev','mgr']
    print('')

    # use the _asdict() method to convert an convert a namedtuple-generated
    # object to a 'dictoinary-like' object
    bd = bob._asdict()  # dictionary from namedtuple "OrderedDict"
    # {'name':'Bob','age':40.5,'jobs':['dev','mgr']}
    print(bd)
    print(bd['name'], bd['jobs'])  # Bob ['dev','mgr']
    print('')

    bob = Rec('Bob', 40.5, ['dev', 'mgr'])
    name, age, jobs = bob  # assignment to tuple
    print(bob)
    print(name, age, jobs)  # Bob 40.5 ['dev','mgr']
    print('')

    # iteration
    for x in bob:
        print(x, end=' ')  # Bob 40.5 ['dev','mgr']
    print('\n')

    bob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
    job, name, age = bob.values()
    print(bob)
    print(job, name, age)  # Bob 40.5 ['dev','mgr']
    print('')

    for x in bob:
        print(bob[x], end=' ')  # Bob 40.5 ['dev','mgr']
    print('\n')

    # alternatively
    for x in bob.values():
        print(x, end=' ')  # Bob 40.5 ['dev','mgr']
