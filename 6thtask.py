def swap(func):
    def wrapper(*args, **kwargs):  # Unnamed and named args respectively. Kwargs have to be after args!
        args = reversed(args)
        func(*args, **kwargs)
    return wrapper


@swap
def div(x, y, show=False):  # Default value is False
    res = x / y
    if show:
        print(res)
    return res


if __name__ == "__main__":
    div(2, 4, show=True)
