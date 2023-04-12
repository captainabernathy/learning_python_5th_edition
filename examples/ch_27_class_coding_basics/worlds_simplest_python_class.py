class rec:
    pass  # empty namespace object


def uppername(obj):
    return obj.name.upper()


if __name__ == "__main__":
    # add attributes to rec directly
    rec.name = 'Bob'
    rec.age = 40

    print(rec.name)  # Bob
    print(rec.age)  # 40
    print('')

    x = rec()  # instances inherit class names
    y = rec()
    print(x.name, y.name)  # 'Bob' 'Bob'... name stored in class

    x.name = 'Sue'  # changes instance's value
    print(rec.name, x.name, y.name)  # Bob Sue Bob
    print('')

    # ['__module__', '__dict_', '__weakref__', '__doc__', 'name', 'age']
    print(list(rec.__dict__.keys()))  # class attributes ^^^
    print('')

    # ['name', 'age']
    print(list(name for name in rec.__dict__ if not name.startswith('__')))

    print(list(x.__dict__.keys()))  # ['name']... only attributed filled out
    print(list(y.__dict__.keys()))  # []... empty
    print('')

    print(x.name)  # Sue... access attribute directly
    print(x.__dict__['name'])  # Sue... access from dictionary by key
    print(x.age)  # 40... age retrieved from class

    try:
        print(x.__dict__['age'])  # age not set in object, so this is an error
    except KeyError as ex:
        print("KeyError:", ex)
    print('')

    print(x.__class__)  # <class '__main__.rec'>... instance to class link
    print(rec.__bases__)  # (<class 'object'>,)... class to superclass link
    print('')

    print(uppername(rec))  # BOB... uses rec's name class value 'Bob'
    print(uppername(x))  # SUE... uses x's name value
    print(uppername(y))  # BOB... uses rec's name class value 'Bob'
    print('')

    # add a method named method to rec that aliases the function uppername()
    rec.metho = uppername
    print(rec.metho(rec))  # BOB... argument required to call from class
    print(x.method())  # SUE... equivalent to rec.method(x)
    print(y.method())  # BOB... uses rec's name class value 'Bob'
    print('')

    print(rec.method(x))  # SUE call through class
    print(rec.method(y))  # BOB
