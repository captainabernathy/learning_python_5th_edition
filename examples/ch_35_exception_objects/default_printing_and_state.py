# usage: python3 default_printing_and_state.py

# NOTE: by default instances of class-based exceptions display whatever is
# passed to the class constructor when they are caught (and printed)
class E(Exception):
    pass


if __name__ == '__main__':
    print('code snippets from pages 1172-1173\n')

    try:
        raise IndexError  # same as raise IndexError()
    except IndexError as ex:
        print(ex)  # empty... same as ex.__str__() or str(ex)
        print(ex.args)  # ()
        print(repr(ex))  # IndexError()... same as ex.__repr__()
    print('')

    try:
        raise IndexError('spam')
    except IndexError as ex:
        print(ex)  # spam... same as ex.__str__() or str(ex)
        print(ex.args)  # ('spam',)
        print(repr(ex))  # IndexError('spam')... same as ex.__repr__()
    print('')

    Ex = IndexError('spam')
    print(Ex)  # spam... same as Ex.__str__() or str(Ex)
    print(Ex.args)  # ('spam',)
    print(repr(Ex))  # IndexError('spam')... same as repr(Ex)
    print('')

    try:
        raise E
    except Exception as ex:
        print(ex)  # empty... same as ex.__str__() or str(ex)
        print(ex.args)  # ()
        print(repr(ex))  # E()... same as repr(ex)
    print('')

    try:
        raise E('Espam')
    except Exception as ex:
        print(ex)  # Espam... same as ex.__str__() or str(ex)
        print(ex.args)  # ('Espam')
        print(repr(ex))  # E('Espam')... same as repr(ex)
    print('')

    Ex = E('Espam')
    print(Ex)  # Espam... same as Ex.__str__() or str(Ex)
    print(Ex.args)  # ('Espam',)
    print(repr(Ex))  # E('Espam')... same as repr(Ex)
    print('')

    try:
        raise E('spam', 'eggs', 'ham')
    except E as Ex:
        print(Ex)  # ('spam','eggs','ham')... same as Ex.__str__() or str(Ex)
        print(Ex.args)  # ('spam','eggs','ham')
        print(repr(Ex))  # E('spam','eggs','ham')... same as Ex.__repr__()
