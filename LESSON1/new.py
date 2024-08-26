globalVar = 1


def printGlobal():
    print(globalVar)


def printLocal():
    local = 2
    print(local)
    print(globalVar)


printGlobal()
printLocal()
