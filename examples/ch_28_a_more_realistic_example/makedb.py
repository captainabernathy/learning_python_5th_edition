# program stores a Person object on a shelve database
# NOTE: the shelve module allows you to store pickled objects by key
import shelve
from person import Person
from person import Manager

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)

    db = shelve.open('persondb')  # filename where objects are stored
    for obj in (bob, sue, tom):  # use object's name attr as key
        db[obj.name] = obj  # store object on shelve by key
    db.close()  # close after making changes
