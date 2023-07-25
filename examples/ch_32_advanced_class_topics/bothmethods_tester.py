from bothmethods import Methods


if __name__ == '__main__':
    print('code snippets from page 1065\n')

    obj = Methods()

    # instance method called through object... implicitly passed self reference
    obj.imeth(1)  # <botmethods.Methods object at Ox...> 1

    # instance method called through class... requires object to be passed
    Methods.imeth(obj, 2)  # <bothmethods.Methods object at 0x...> 2
    print('')

    Methods.smeth(3)  # [3]... static method called through class

    obj.smeth(4)  # [4]... static method called through instance
    print('')

    # class method called through class... implicitly passed a reference to the
    # class
    Methods.cmeth(5)  # [<class 'bothmethods.Methods'>,5]

    # class method called through instance... implicitly passed a reference to
    # the class
    obj.cmeth(6)  # [<class 'bothmethods.Methods'>,6]
