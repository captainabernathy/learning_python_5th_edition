# usage: python3 comparisons_normal_and_chained.py

if __name__ == '__main__':
    print('code snippets from pages 149-150\n')

    print(1 < 2)  # True
    print(2.0 >= 1)  # True
    print(2.0 == 2.0)  # True
    print(2.0 != 2.0)  # False
    print('')

    X = 2
    Y = 4
    Z = 6
    # chained comparisons
    print(X < Y < Z)  # True
    print(X < Y and Y < Z)  # True
    print('')

    print(X < Y > Z)  # False
    print(X < Y and Y > Z)  # False
    print(1 < 2 < 3.0 < 4)  # True
    print(1 > 2 > 3.0 > 4)  # False
    print('')

    print(1 == 2 < 3)  # False... same as 1 == 2 && 2 < 3
    print('')

    print(1.1 + 2.2 == 3.3)  # False... bc floating point arithmetic
    print(1.1 + 2.2)  # 3.300...03
    print(int(1.1 + 2.2) == int(3.3))  # True... truncate float to int
