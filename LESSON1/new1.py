def funcA():
    print("Start A")
    funcB()
    print("End A")


def funcB():
    print("Start B")
    funcC()
    print("End B")


def funcC():
    print("Start C")
    funcD()
    print("End C")


def funcD():
    print("Start D")

    print("End D")


# funcA()


def endless():
    print("endless")
    endless()


endless()
