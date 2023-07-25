# NOTE: __slots__ are a class attribute that contains a list of names that
# limits the set of legal attributes that an instance of the class will have...
# only the names in the slots list can be assigned instance attributes
class limiter(object):
    __slots__ = ['age', 'name', 'job']


if __name__ == '__main__':
    print('code snippets from pages 1045-1046\n')

    x = limiter()

    try:
        print(x.age)  # attributes must be assigned before they can be accessed
    except AttributeError as ex:
        print('Error:', ex)  # Error: 'limiter' object has no attribute 'age'
    print('')

    x.age = 40  # initilize age attribute
    print(x.age)  # 40
    print('')

    try:
        x.ape = 1000  # illegal... ape is not one of limiter's slots
    except AttributeError as ex:
        print(ex)  # 'limiter' object has not attribute 'ape'
    print('')
