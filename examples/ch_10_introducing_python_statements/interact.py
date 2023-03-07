if __name__ == '__main__':
    print('covers code examples from pages 340-347\n')

    # prompt user for input, convert input to upper-case, and display the
    # result
    # continue prompting until user types "stop"
    print('test1')
    while True:
        reply = input('Enter a line of text or "stop" to quit: ')
        if reply == 'stop':
            break
        print(reply.upper())  # display input converted to upper-case
    print('')

    # prompt user for an integer, square it, and display the result
    # continue prompting until user types "stop"
    # NOTE: invalid input will crash program
    print('test2')
    while True:
        reply = input('Enter an integer or "stop" to quit: ')
        if reply == 'stop':
            break
        else:
            print(int(reply) ** 2)  # convert input to int, square, and display
    print('')

    # prompt user for integer, square it, and display the result
    # notify user when invalid is entered, and re-prompt
    # continue prompting until user types "stop"
    print('test3')
    while True:
        reply = input('Enter an integer of "stop" to quit: ')
        if reply == 'stop':
            break
        elif not reply.isdigit():  # do not operate on invalid input
            print('Bad!' * 8)  # notify user
        else:
            print(int(reply) ** 2)  # convert input to int, square, and display
    print('')

    # prompt user for integer, square it, and display the result
    # catch invalid input as an Exception, notify user, and re-prompt
    # continue prompting until user types "stop"
    print('test4')
    while True:
        reply = input('Enter an integer or "stop" to quit: ')
        if reply == 'stop':
            break
        try:
            num = int(reply)  # try to convert input to int
        except Exception:  # conversion failed
            print('Bad!' * 8)  # notify user
        else:
            print(num ** 2)  # square and display
    print('')

    # prompt user for integer, square it, and display the result
    # catch invalid input as an Exception, notify user, and re-prompt
    # continue prompting until user types "stop"
    print('test5')
    while True:
        reply = input('Enter an integer or "stop" to quit: ')
        if reply == 'stop':
            break
        try:  # try to convert input to int, sqaure and display
            print(int(reply) ** 2)
        except Exception:  # conversion failed
            print('Bad!' * 8)  # notify user
    print('')

    # prompt user for a floating point value, square it, and display the result
    # catch invalid input as an Exception, notify user, and re-prompt
    # continue prompting until user types "stop"
    print('test6')
    while True:
        reply = input('Enter text: ')
        if reply == 'stop':
            break
        try:  # try to convert input to float, square, and display
            print(float(reply) ** 2)
        except Exception:  # conversion failed
            print('Bad!' * 8)  # notify user
    print('')

    # prompt user for an integer >= 20, square it, and display the result
    # notify user in cases of input that is invalid or less that 20
    # continue prompting until user types "stop"
    print('test7')
    while True:
        reply = input('Enter an integer >= 20 or "stop" to quit: ')
        if reply == 'stop':
            break
        elif not reply.isdigit():  # do not operate on invalid input
            print('Bad!' * 8)
        else:
            num = int(reply)  # convert input
            if num < 20:  # do not operate on input < 20
                print('low')  # notify user
            else:
                print(num ** 2)  # square and display
