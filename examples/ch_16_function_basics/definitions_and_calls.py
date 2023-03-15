# a simple function that returns the product of two arguments for any type
# that defines multiplication
def times(x, y):
    return x * y


if __name__ == '__main__':
    print('code snippets from page 467\n')
    print(times(2, 4))  # 8

    x = times(3.14, 4)
    print(x)  # 12.56

    # works for any type that defines multiplication
    print(times('Ni', 4))  # NiNiNiNi
