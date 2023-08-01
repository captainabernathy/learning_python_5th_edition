# augmenting decorated objects directly
def decorate(func):
    func.marked = True
    return func


@decorate
def spam1(a, b):  # spam1 = decorate(spam1)
    return a + b


# similar to decorate^^^, but value is decorator argument
def annotate(text):
    def decorate(func):
        func.label = text
        return func
    return decorate


@annotate('spam data')
def spam2(a, b):
    # spam2 = annotate('spam data')(spam)
    return a + b


# for illustrative purposes...
def spam3(a, b):
    return a + b


if __name__ == '__main__':
    print('code snippets from pages 1359-1360\n')

    print(spam1.marked)  # True
    print('')

    # for illustrative purposes...
    sd1 = decorate(spam3)
    print(sd1.marked)
    print('')

    print(spam2(1, 2))  # 3
    print('')

    print(spam2.label)  # spam data
    print('')

    # for illustrative purposes
    sa1 = annotate('spam data')(spam3)

    print(sa1(1, 2))  # 3
    print('')

    print(sa1.label)  # spam data
    print('')
