# function recursively computes the sum of a list of numbers and returns the
# result
def mysum1(L):
    if not L:
        return 0
    else:
        return L[0] + mysum1(L[1:])


# same as mysum1() but written using a ternary expression
def mysum2(L):
    return 0 if not L else L[0] + mysum2(L[1:])


# function recursively computes the sum of a list of elements that defines the
# a + operation
def mysum3(L):
    return L[0] if len(L) == 1 else L[0] + mysum3(L[1:])


# same as mysum4() but written using ternary expression
def mysum4(L):
    first, *rest = L
    return first if not rest else first + mysum4(rest)


# function computes the sum of a list of numbers via indirect recursion
def mysum5(L):
    if not L:
        return 0
    return nonempty(L)  # indirect recursion


# performs the recursive action of mysum5()
def nonempty(L):
    return L[0] + mysum5(L[1:])


if __name__ == '__main__':
    print('code snippets from pages 578-580\n')
    print(mysum1([1, 2, 3, 4, 5]))  # 15
    print(mysum2([1, 2, 3, 4, 5]))  # 15
    print(mysum3([1, 2, 3, 4, 5]))  # 15
    print(mysum4([1, 2, 3, 4, 5]))  # 15
    print(mysum5([1, 2, 3, 4, 5]))  # 15
    print('')

    print(mysum3(['s', 'p', 'a', 'm']))  # spam
    print(mysum4(['s', 'p', 'a', 'm']))  # spam
    print('')

    print(mysum3(['spam', 'ham', 'eggs']))  # spamhameggs
    print(mysum4(['spam', 'ham', 'eggs']))  # spamhameggs
    print('')

    # via loops
    L = [1, 2, 3, 4, 5]
    s = 0
    while L:
        s += L[0]
        L = L[1:]

    print(s)  # 15

    L = [1, 2, 3, 4, 5]
    s = 0
    for x in L:
        s += x

    print(s)  # 15
