# NOTE: make sure to run makedb.py before running this program
import glob  # glob enables you to get directory listings in python code
import shelve

if __name__ == '__main__':

    # ['person_department.py', 'person_composite.py', 'persondb', 'person.py']
    print(glob.glob('person*'))
    print('')

    # NOTE: when python pickles a class instance, it records the class's self
    # instance attributes, along with the name of the class it was created from
    # and the module where the class lives... so class instances automatically
    # all their class behavior when they are later loaded, and it is only
    # necessary to import classes to make new objects
    db = shelve.open('persondb')
    print(len(db))  # 3... number of records
    print(list(db.keys()))  # ['Tom Jones', 'Sue Jones', 'Bob Smith']...
                            # keys in index
    print('')

    bob = db['Bob Smith']

    # NOTE: pickle-able classes must be coded at the top level of a module file
    # accessible from a directory listed on the sys.path module's search path..
    # also, any changes in a pickle-able's class's source code is automatically
    # picked up when instances are unpickled... w/o needing to update the
    # stored objects themselves
    print(bob.last_name())  # Smith
    print('')

    # Tom Jones => [Manager: job=mgr, name=Tom Jones, pay=50000]
    # Sue Jones => [Person: job=dev, name=Sue Jones, pay=100000]
    # Bob Smith => [Person: job=None, name=Bob Smith, pay=0]
    for key in db:
        print(key, '=>', db[key])
    print('')

    # Bob Smith => [Person: job=None, name=Bob Smith, pay=0]
    # Sue Jones => [Person: job=dev, name=Sue Jones, pay=100000]
    # Tom Jones => [Manager: job=mgr, name=Tom Jones, pay=50000]
    for key in sorted(db):
        print(key, '=>', db[key])
