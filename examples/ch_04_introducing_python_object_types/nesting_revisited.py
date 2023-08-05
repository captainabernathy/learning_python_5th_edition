# usage: python3 nesting_revisited.py

if __name__ == '__main__':
    print('code snippets from pages 117-118\n')

    # nested dictionary
    rec = {'name': {'first': 'Bob', 'last': 'Smith'},
           'jobs': ['dev', 'mgr'],
           'age': 40.5}

    print(rec)

    # name is a nested dictionary
    print(rec['name'])  # {'first':'Bob', 'last':'Smith'}

    # index into name
    print(rec['name']['last'])  # Smith

    # jobs is a nested list
    print(rec['jobs'])  # ['dev','mgr']

    # index into the list
    print(rec['jobs'][-1])  # mgr

    # expand list in place
    rec['jobs'].append('janitor')
    print(rec['jobs'])  # ['dev', 'mgr', 'janitor']
