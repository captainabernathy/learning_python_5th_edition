# usage: python3 scopes_lambdas_can_be_nested_too.py

# function that returns a lambda function that returns the sum of the argument
# passed to it and the argument passed to the lambda
def action(x):
    return (lambda y: x + y)  # make and return function... remember x


if __name__ == '__main__':
    print('code snippets from page 595\n')

    act = action(99)
    print(act(2))  # 101

    # alternatively... nested lambda functions in a single statement
    action = (lambda x: (lambda y: x + y))

    act = action(99)
    print(act(3))  # 102

    # or... just call the nested lambda function immediately
    print((lambda x: (lambda y: x + y))(99)(4))
