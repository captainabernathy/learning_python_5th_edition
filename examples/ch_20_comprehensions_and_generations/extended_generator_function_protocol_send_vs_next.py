# usage: python3 extended_generator_function_protocol_send_vs_next.py

def gen():
    for i in range(10):
        # NOTE: when used in an assignment statement, a yield expression must
        # be enclosed in parentheses unless it is the only item on the
        # right-hand side of the statement
        X = yield i
        print(X)


if __name__ == '__main__':
    print('code snippets from page 619\n')

    # NOTE: technically yield is an expression (since 2.5) that returns the
    # item passed to send()... NOT a statement
    # send() advances to the next item in a series of results like __next__(),
    # but also provides a way for the caller to communicate with the generator
    G = gen()
    i = next(G)
    print(i)  # 0
    i = G.send(77)  # 77... send value to generator
    print(i)  # 1
    i = G.send(88)  # 88
    print(i)  # 2
    i = next(G)  # None... nothing sent to the function to print
    print(i)  # 3
