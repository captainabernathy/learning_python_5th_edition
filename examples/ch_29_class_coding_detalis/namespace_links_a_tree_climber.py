import classtree


class Emp:
    pass


class Person(Emp):
    pass


if __name__ == '__main__':
    print('code snippets from page 910\n')
    bob = Person()
    classtree.instancetree(bob)
