class Person:

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


if __name__ == '__main__':
    print('code snippets from pages 851-853\n')
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob.name, bob.pay)  # Bob Smith 0
    print(sue.name, sue.pay)  # Sue Jones 100000
    print(bob.last_name(), sue.last_name())  # Smith Jones

    sue.give_raise(.10)
    print(sue.pay)  # 110000
