import argparse


def fibonacci(n):
    n = int(n)
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# наслаиваем на парсер с класса ArgumentParser информацию об ожидаемом аргументе из командной строки
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num', nargs='?')
    return parser


if __name__ == "__main__":

    parser = createParser()  # создаем наш парсер
    object_to_parse = parser.parse_args()  # сохраняем объект с аргументами с помощью парсинга командной строки
    print(fibonacci(object_to_parse.num))
