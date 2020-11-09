def func(num):  # Some random bad function
    return str(num) + " ha"


def print_map(func, iter):
    print(*(map(func, iter)), sep='\n')


if __name__ == "__main__":
    print_map(func, [1, 2, 3])

