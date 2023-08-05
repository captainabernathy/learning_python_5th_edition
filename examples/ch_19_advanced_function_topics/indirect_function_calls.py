# usage: python3 indirect_function_calls.py

# simple function that prints the message it receives
def echo(msg):  # name echo assigned to function object
    print(msg)


# function calls the argument passed into func with the agrument passed into
# arg
def indirect(func, arg):
    func(arg)  # call passed in object


# function returns a closure that outputs the argument it receives prepended
# with the argument passed to label
def make(label):  # make a function, but don't call it
    def echo(message):
        print(label + ':' + message)
    return echo


if __name__ == '__main__':
    print('code snippets from page 585\n')

    echo('Direct call')  # Direct call
    x = echo
    x('Indirect call')  # Indirect call

    indirect(echo, 'Argument call')  # Argurment call
    print('')

    schedule = [(echo, 'Spam!'), (echo, "Ham!")]
    for (func, arg) in schedule:
        func(arg)  # call functions embedeed in containers
    print('')

    F = make('Spam')
    F('Ham!')  # Spam:Ham!
    F('Eggs!')  # Spam:Eggs!
