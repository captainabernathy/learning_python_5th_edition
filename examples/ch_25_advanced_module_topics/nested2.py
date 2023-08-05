# usage: python3 nested1.py

# NOTE: if you import two names using from in another module, you get copies
# of them
from nested1 import X
from nested1 import printer

X = 88  # changes local copy of X... nested1's X remains unchanged

if __name__ == '__main__':
    print('code snippets from page 797.\n')

    printer()  # 99... prints nested1's X
    print(X)  # 88... local X
