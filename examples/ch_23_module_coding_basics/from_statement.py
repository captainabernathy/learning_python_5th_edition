# usage: python3 from_statement.py

from module1 import printer  # import the name of the component from a module

if __name__ == '__main__':
    print('code snippets from page 713\n')

    # NOTE: when a component is imported from a module in a from statement, it
    # is not necessary to qualify the name
    printer('Hello world!')
