from first_example import FirstClass


# SecondClass inherits from FirstClass
class SecondClass(FirstClass):
    # overrides FirstClass's display() method
    def display(self):
        print('Current value = %s' % self.data)


if __name__ == "__main__":
    x = FirstClass()
    x.setdata('New value')

    z = SecondClass()
    z.setdata(42)
    z.display()  # Current value = 42... calls overridden display() method

    x.display()  # New value
