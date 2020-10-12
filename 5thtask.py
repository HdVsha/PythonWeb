# def decorator_maker():
#     print("Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать декоратор.")
#     def my_decorator(func):
#         print("Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")
#         def wrapped():
#             print("Я - обёртка вокруг декорируемой функции.\n"
#                   "Я буду вызвана каждый раз, когда ты вызываешь декорируемую функцию.\n"
#                   "Я возвращаю результат работы декорируемой функции.")
#             return func()
#         print("Я возвращаю обёрнутую функцию.")
#         return wrapped
#     print("Я возвращаю декоратор.")
#     return my_decorator
#
# @decorator_maker()
# def decorated_function():
#     print("Я - декорируемая функция.")


def decorator(func):
    def wrapper(nums):
        res = func(nums)
        if res == 0:
            return 'Нет('
        elif res > 10:
            return 'Слишком много'
        else:
            return res
    return wrapper


@decorator
def even_func(array):
    counter = 0
    for el in array:
        if el % 2 == 0:
            counter += 1
    return counter


if __name__ == "__main__":

    print(even_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 14, 16, 12, 18, 20]))
    print(even_func([1, 3, 5]))
    print(even_func([2, 4, 6]))
