def printUpTo(up, curr=0):
    print(curr)
    if (curr != up):
        printUpTo(up, curr + 1)


printUpTo(30)
