import pickle


def test_pickle(inp):
    with open('file.pickle', 'wb') as f:
        pickle.dump(inp, f)

    with open('file.pickle', 'rb') as f:
        out = pickle.load(f)

    assert type(inp) == type(out)

    if hasattr(inp, '__iter__'):
        assert [i for i in inp] == [j for j in out]
    else:
        assert inp == out

    return "Worked"


if __name__ == "__main__":
    info = iter([range(5)])
    print(test_pickle(info))
    func = print
    print(test_pickle(func))

    #  Что может сохранять модуль pickle?
    #
    # Все встроенные типы данных Python: тип boolean, Integer, числа с плавающей точкой,
    # комплексные числа, строки, объекты bytes, массивы байт, и None.
    # Списки, кортежи, словари и множества, содержащие любую комбинацию встроенных типов данных
    # Списки, кортежи, словари и множества, содержащие любую комбинацию списков, кортежей,
    # словарей и множеств содержащий любую комбинацию встроенных типов данных
    # (и так далее, вплоть до максимального уровня вложенности, который поддерживает Python).
    # Функции, классы и экземпляры классов (с caveats).
