import unders  # gets every named defined in the unders module

if __name__ == '__main__':
    print('code snippets from pages 771-772\n')

    # _names not hidden from import
    print(unders.a, unders._b, unders.c, unders._d)  # 1 2 3 4
