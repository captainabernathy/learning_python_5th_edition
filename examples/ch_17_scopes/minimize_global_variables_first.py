X = 99  # global variable


# updates module's global variable X to the value passed to newX
def setX(newX):
    global X
    X = newX
