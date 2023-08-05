# usage: python3 applying_class_decorators_to_built_in_types.py

from interfacetracer import Tracer


@Tracer
class MyList(list):
    # MyList = Tracer(MyList)
    pass


if __name__ == '__main__':
    print('code snippets from page 1352\n')

    x = MyList([1, 2, 3])  # Triggers Wrapper()
    x.append(4)  # Trace: append... Triggers __getattr__.append
    print('')

    print(x.wrapped)
    print('')

    WrapList = Tracer(list)  # perform decoration manually
    x = WrapList([4, 5, 6])
    x.append(7)  # Trace: append
    print('')

    print(x.wrapped)  # [4,5,6,7]
    print('')
