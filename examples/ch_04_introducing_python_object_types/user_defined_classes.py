class Worker:
    # constructor
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    # return a Worker's last name
    def lastName(self):
        return self.name.split()[-1]

    # give a worker a raise by the given percent
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


if __name__ == '__main__':
    print('code snippets from pages 132-133\n')
    bob = Worker('Bob Smith', 50000)
    sue = Worker('Sue Jones', 60000)
    print(bob.lastName())  # Smith
    print(sue.lastName())  # Jones

    sue.giveRaise(0.10)
    print(sue.pay)  # 66000.0
