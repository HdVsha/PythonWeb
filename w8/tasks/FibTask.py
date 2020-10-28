def fibonacci(num):
    f_1 = 1
    f_2 = 1
    while num != 0:
        yield f_2
        num -= 1
        f_1, f_2 = f_2, f_1 + f_2


for i in fibonacci(7):
    print(i)
