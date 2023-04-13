class Super:
    def hello(self):
        self.data1 = 'spam'


class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'


if __name__ == '__main__':
    print('code snippets from pages 907=908\n')
    X = Sub()
    print(X.__dict__)  # {}... empty dictionary

    # instance of class... class type
    print(X.__class__)  # <class '__main__.Sub'>...

    # subclas of class... class tuple
    print(Sub.__bases__)  # (<class '__main__.Super'>,)

    # class tuple... but... empty tuple in 2.X
    print(Super.__bases__)  # (<class 'object'>,)
    print('')

    Y = Sub()
    X.hello()  # updates X
    print(X.__dict__)  # {data1: 'spam'}

    X.hola()  # updates X
    print(X.__dict__)  # {'data1':'spam', 'data2':'eggs'}
    print('')

    # ['__module__', 'hola', '__doc__']
    print(list(Sub.__dict__.keys()))

    # ['__module__', 'hello', '__dict__', '__weakref__', '__doc__']
    print(list(Super.__dict__.keys()))
    print('')

    print(Y.__dict__)  # {}... empty dictionary
    print('')

    print(X.data1, X.__dict__['data1'])  # spam spam

    X.data3 = 'toast'  # adds attribute to X
    print(X.__dict__)  # {'data1':'spam','data2':'eggs','data3':'toast'}
    print('')

    X.__dict__['data3'] = 'ham'  # update X
    print(X.data3)  # ham
