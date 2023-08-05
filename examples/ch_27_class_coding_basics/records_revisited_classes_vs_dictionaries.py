# usage: python3 records_revisited_classes_vs_dictionaries.py

from collections import namedtuple


class rec3:
    pass


class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return (self.name, self.jobs)


if __name__ == '__main__':
    print('code snippets from pages 839-841\n')

    rec1 = ('Bob', 40.5, ['dev', 'mgr'])  # tuple-based record
    print(rec1)  # ('Bob',40.5,['dev','mgr'])
    print(rec1[0])  # Bob
    print(rec1[1])  # 40.5
    print(rec1[2])  # ['dev', 'mgr']
    print('')

    rec2 = {}  # dictionary-based record
    rec2['name'] = 'Bob'
    rec2['age'] = 40.5
    rec2['jobs'] = ['dev', 'mgr']
    print(rec2)  # {'name':'Bob','age':40.5,'jobs':['dev','mgr']}
    print(rec2['name'])  # Bob
    print(rec2['age'])  # 40.5
    print(rec2['jobs'])  # ['dev','mgr']
    print('')

    pers1 = rec3()  # instance-based records
    # give pers1 some attributes
    pers1.name = 'Bob'
    pers1.jobs = ['dev', 'mgr']
    pers1.age = 40.5
    print(pers1.name)  # Bob
    print(pers1.age)  # 40.5
    print(pers1.jobs)  # ['dev','mgr']
    print('')

    pers2 = rec3()
    # give pers2 some attributes
    pers2.name = 'Sue'
    pers2.jobs = ['dev', 'cto']
    print(pers2.name)  # Sue
    print(pers2.jobs)  # ['dev','cto']
    print('')

    # instantiate some person objects
    rec4 = Person('Bob', ['dev', 'mgr'], 40.5)
    rec5 = Person('Sue', ['dev', 'cto'])

    print(rec4.jobs)  # ['dev','mgr']
    print(rec5.info())  # ('Sue',['dev','cto'])
    print('')

    # instantiate a dictionary-based record
    rec6 = dict(name='Bob', age='40.5', jobs=['dev', 'mgr'])
    print(rec6['name'])  # Bob
    print(rec6['age'])  # 40.5
    print(rec6['jobs'])  # ['dev','mgr']
    print('')

    # same as ^
    rec7 = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
    print(rec7['name'])  # Bob
    print(rec7['age'])  # 40.5
    print(rec7['jobs'])  # ['dev','mgr']
    print('')

    # similarly with a namedtuple
    Rec = namedtuple('Rec', ['name', 'age', 'jobs'])  # a generalized class
    rec8 = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])
    print(rec8.name, rec8[0])  # Bob Bob
    print(rec8.age, rec8[1])  # 40.5 40.5
    print(rec8.jobs, rec8[2])  # ['dev','mgr'] ['dev','mgr']
