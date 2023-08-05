# usage: python3 truth_values_and_boolean_tests.py

if __name__ == '__main__':
    print('code snippets from page 394\n')

    print(2 < 3, 3 < 2)  # True, False

    # NOTE: for tests with or, python returns the first operand that evalutes
    # to True or the right operand if neither operand operates to True
    print(2 or 3, 3 or 2)  # 2 3
    print([] or 3)  # 3
    print([] or {})  # {}
    print('')

    # NOTE: for tests with and, if both operands evaluate to True, python will
    # return the last operand... otherwise, if the expression evaluates to
    # False, python will return the frist element that evaluates to False
    print(2 and 3, 3 and 2)  # 3 2
    print([] and {})  # []
    print(3 and [])  # []
