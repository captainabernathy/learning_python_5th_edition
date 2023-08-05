# usage: python3 oop_and_delegation_wrapper_proxy_objects.py

from trace import Wrapper


if __name__ == '__main__':
    print('code snippets from page 973\n')

    x = Wrapper([1, 2, 3])  # wrap a list
    x.append(4)  # delegate to a list method
    print(x.wrapped)  # Trace: append [1,2,3,4]
    print('')

    x = Wrapper({'a': 1, 'b': 2})  # wrap a dictionary
    #  delegate to dictionary method
    print(list(x.keys()))  # Trace: keys ['a','b']
