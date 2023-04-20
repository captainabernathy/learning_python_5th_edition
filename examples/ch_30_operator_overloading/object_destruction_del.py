# NOTE: the __del__() method is run automatically at garbage collection time

class Life:
    def __init__(self, name='unknown'):
        print('Hello,', name)
        self.name = name

    def live(self):
        print(self.name)

    def __del__(self):
        print('Goodbye ' + self.name)


if __name__ == '__main__':
    print('code snippets from page 959\n')
    brian = Life('Brian')  # Hello, Brian
    brian.live()  # Brian
    brian = 'bob'  # Goodbye Brian... since object is reclaimed
