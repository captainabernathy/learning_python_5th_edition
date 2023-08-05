# usage: python3 if_else_ternary_expression.py

if __name__ == '__main__':
    print('code snippets from page 395\n')

    # NOTE: non-empty strings evaluate to True, and empty strings evaluate to
    # False
    A = 't' if 'spam' else 'f'
    print(A)  # t

    A = 't' if '' else 'f'
    print(A)  # f
