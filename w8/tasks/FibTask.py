def fibo_gen():
    f_1, f_2 = 1, 1
    while True:
        yield f_2
        f_1, f_2 = f_2, f_1 + f_2


def fib_convert(num):
    a = []
    f = fibo_gen()
    for i in range(num):
        a.append(next(f))
    return a


