# usage: python3 nested3.py

# NOTE: if you use import to get an entire module and then assign to a
# qualified name, you change the value in of that name in the module's scope
# as well
import nested1

nested1.X = 88  # changes nested1's X directly

if __name__ == '__main__':
    print('code snippets from page 797.\n')

    nested1.printer()  # 88... no longer 77... change reflected
