def c():
    print("last call")
    raise ValueError("my exception")


def b():
    print("second call")
    c()


def a():
    print("first call")
    b()


if __name__ == "__main__":
    a()
