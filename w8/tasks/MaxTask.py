from itertools import accumulate


def maximize(lists, m):
    maximums_sqrd = [max(array)**2 for array in lists]
    res = [el for el in accumulate(maximums_sqrd)]

    return max([x % m for x in res])


def test_maximize():
    lists = [
        [5, 4],
        [7, 8, 9],
        [5, 7, 8, 9, 10]
    ]
    assert maximize(lists, m=1000) == 206

    lists = [
        [1000, 4],
        [7, 8, 9],
        [5, 7, 8, 9, 10]
    ]
    assert maximize(lists, m=1000) == (1000 ** 2 + 9 ** 2 + 10 ** 2) % 1000

    lists = [
        [1, 1],
        [1, 2],
        [0, 3]
    ]
    assert maximize(lists, 10) == (1 ** 2 + 2 ** 2) % 10


if __name__ == "__main__":
    test_maximize()
