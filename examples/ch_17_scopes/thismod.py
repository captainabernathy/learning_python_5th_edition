var = 99  # global variable (module attribute)


def local():
    var = 0  # change local var


# function updates module's global var variable
def glob1():
    global var  # change global var
    var += 1


# function imports this module to access and update its global var variable
def glob2():
    var = 0  # change local var
    import thismod  # import this file
    thismod.var += 1  # change global var


# function updates this module's global var variable by importing the sys
# module and looking up thismod in the sys module's modules dictionary
def glob3():
    var = 0  # change local var
    import sys  # import system table
    glob = sys.modules['thismod']  # get module object
    glob.var += 1  # change global var


# tester function that calls the various function defined above
def test():
    print(var)  # 99
    local()  # doesn't updat var
    glob1()  # var is now 100
    glob2()  # var is now 101
    glob3()  # var is now 102
    print(var)  # 102
