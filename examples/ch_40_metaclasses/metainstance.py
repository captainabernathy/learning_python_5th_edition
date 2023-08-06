# usage: python3 metainstance.py

print('code snippets from pages 1426-1427\n')


class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', classname)
        return type.__new__(meta, classname, supers, classdict)

    def toast(self):
        return 'toast'


# In MetaOne.new: Super
class Super(metaclass=MetaOne):
    def spam(self):
        return 'spam'


# InMetaOne.new: Sub
class Sub(Super):
    def eggs(self):
        return 'eggs'


if __name__ == '__main__':
    X = Sub()  # normal instance of user-defined class
    print('')

    print(X.eggs())  # eggs
    print(X.spam())  # spam... inherited from Super
    print('')

    try:
        print(X.toast())  # ERROR: toast() is a class method... not instance!
    except AttributeError as ex:
        print(ex)  # 'Sub' object has no attribute 'toast'
    print('')

    print(Sub.eggs(X))  # eggs
    print(Sub.spam(X))  # spam
    print('')

    print(Sub.toast())  # toast... called through class
    print('')

    try:
        print(Sub.toast(X))  # ERROR: toast() cannot be called through instance
    except TypeError as ex:
        print(ex)
    print('')

    # NOTE: Methods acquired from metaclasses are bound to the subject class...
    # HOWEVER methods from normal classes are unbound if accessed through the
    # class but bound when fetched through the instance
    print(Sub.toast)  # <bound method MetaOne.toast of <class '__main__.Sub'>>
    print('')

    print(Sub.spam)  # <function Super.spam at 0x...>
    print('')

    print(X.spam)  # <bound method Super.spam of <__main__.Sub object at 0x..>>
    print('')

