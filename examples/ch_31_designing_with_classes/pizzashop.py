# usage: python(2/3) pizzashop.py

from __future__ import print_function  # for 2.X/3.X interoperability
from employees import PizzaRobot
from employees import Server


class Customer:
    # constructor initializes this Customer with a name attribute as specified
    def __init__(self, name):
        self.name = name

    # outputs this Customer's order message
    def order(self, server):
        print(self.name, 'orders from', server)

    # outputs this Customer's pay message
    def pay(self, server):
        print(self.name, 'pays for item to', server)


class Oven:
    # outputs this Oven's bake message
    def bake(self):
        print('oven bakes')


class PizzaShop:
    # constructor initializes this PizzaShop's server, chef and oven attributes
    def __init__(self):  # embbeds server, shef, and oven objects
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    # processes an order from a customer with the specified name
    def order(self, name):
        customer = Customer(name)  # initialize a customer
        customer.order(self.server)  # customer orders from server
        self.chef.work()  # perform actions with embedded objects
        self.oven.bake()
        customer.pay(self.server)  # customer pays server


if __name__ == '__main__':
    print('code snippets from pages 967-968\n')

    scene = PizzaShop()  # build a new PizzaShop
    scene.order('Homer')  # process an order from Homer
    print('\n...\n')
    scene.order('Shaggy')  # process an order from Shaggy
