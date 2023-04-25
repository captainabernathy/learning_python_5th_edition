import lister


if __name__ == '__main__':
    print('code snippets from page 1007\n')

    print(lister.ListInstance)  # <class 'listinstance.ListInstance'>
    print('')
    print(lister.Lister)  # <class 'listree.ListTree'>

    from lister import Lister
    print(Lister)  # <class 'listtree.ListTree'>
    print('')

    from lister import ListInstance as Lister
    print(Lister)  # <class 'listinstance.ListInstance'>
