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
