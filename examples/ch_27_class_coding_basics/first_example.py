class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


if __name__ == "__main__":
    print('code snippet from pages 825-827\n')
    x = FirstClass()
    y = FirstClass()

    x.setdata("King Arthur")
    y.setdata(3.14159)

    x.display()  # King Arthur
    y.display()  # 3.14159
    print('')

    x.data = 'New value'  # set attribute directly
    x.display()  # New value
    print('')

    x.anothername = 'spam'  # set a new attribute in x
    print(x.anothername)  # 'spam'
