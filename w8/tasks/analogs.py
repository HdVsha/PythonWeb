import numpy as np


def zip_analog(*iters):  # * bc zip can receive more than 2 iterables
    iterables = [iter(it) for it in iters]  # Making them able to be used with next
    while iterables:
        res = []
        for it in iterables:
            value = next(it, object())  # To avoid stop StopIteration problem value is filled with empty object
            res.append(value)
        yield tuple(res)


def test_zip():
    a = ['a', 'b', 'c', 'd']
    b = [1, 2, 3, 4]
    c = (1, 2, 4, 5)
    for pair in zip(zip_analog(a, b, c), zip(a, b, c)):  # Such a beauty
        assert pair[0] == pair[1]


def enum_analog(iterable, start=0):
    num = start
    for elem in iterable:
        yield num, elem
        num += 1


def test_enum():
    array1 = [10, 12, 13, 14]
    array2 = ['a', 'b', 'c']
    for array in [array1,array2]:
        for pair in zip(enum_analog(array), enumerate(array)):
            assert pair[0] == pair[1]


def map_analog(func, iterable):
    for el in iterable:
        yield func(el)


def test_map():
    f = np.cos
    iterable1 = [1, 2, 3]
    iterable2 = (1, 2, 3)
    for iterable in [iterable1, iterable2]:
        for pair in zip(map_analog(f, iterable), map(f, iterable)):
            assert pair[0] == pair[1]


if __name__ == "__main__":
    test_zip()
    test_enum()
    test_map()