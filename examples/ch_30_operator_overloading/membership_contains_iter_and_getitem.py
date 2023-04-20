from contains import Iters

if __name__ == '__main__':
    print('code snippets from pages 937-938\n')

    X = Iters('spam')
    print(X[0])  # get[0]:s
    print(X[1:])  # get[slice(1,None,None)]:pam
    print('spam'[slice(1, None)])  # pam
    print(X[1:])  # get[slice(1,None,None)]:pam
    print(X[:-1])  # get[slice(None,-1,None)]:spa
    print(list(X))  # iter=>next:next:next:next:next:['s','p','a','m']
