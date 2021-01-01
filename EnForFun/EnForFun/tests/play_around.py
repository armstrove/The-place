


def mygen():
    print("First line")
    yield 1
    print("Second line")
    yield 2
    print("Third line")
    print("4Third line")


x=mygen()
print("1x=<%s>" % (list(x)))

