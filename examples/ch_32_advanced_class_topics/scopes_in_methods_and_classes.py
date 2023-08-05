# usage: python3 scopes_in_methods_and_classes.py

def generate(label):  # returns a class instead of an instance
    class Spam:
        count = 1

        def method(self):
            print('%s=%s' % (label, Spam.count))
    return Spam


if __name__ == '__main__':
    print('code snippets from page 1105\n')

    aclass = generate('Gotchas')
    a = aclass()
    a.method()
