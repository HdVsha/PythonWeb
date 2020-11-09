def fibo_gen():
    f_1, f_2 = 1, 1
    while True:
        yield f_2
        f_1, f_2 = f_2, f_1 + f_2


def fib_convert(num):
    if num == 0:
        raise ValueError("The numeration starts with 1")
    a = []
    f = fibo_gen()
    for i in range(num):
        a.append(next(f))
    return a


