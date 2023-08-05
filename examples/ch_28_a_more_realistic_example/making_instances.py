# usage: python3 making_instances.py

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay


if __name__ == '__main__':
    print('code snippets from pages 846-849\n')

    bob = Person('Bob Smith')  # uses defaults for job and pay
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob.name, bob.pay)  # Bob Smith 0
    print(sue.name, sue.pay)  # Sue Jones 100000
