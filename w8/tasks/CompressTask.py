from itertools import combinations_with_replacement


def get_combinations_with_r(s, n):
    return sorted([''.join(sorted(x)) for x in combinations_with_replacement(s, n)])


def test_get_combinations_with_r():
    assert get_combinations_with_r('cat', 2) == ['aa', 'ac', 'at', 'cc', 'ct', 'tt']
    assert get_combinations_with_r('dog', 3) == ['ddd', 'ddg', 'ddo', 'dgg', 'dgo',
                                                 'doo', 'ggg', 'ggo', 'goo', 'ooo']
    assert get_combinations_with_r('some', 5) == ['eeeee', 'eeeem', 'eeeeo', 'eeees', 'eeemm',
                                                  'eeemo', 'eeems', 'eeeoo', 'eeeos', 'eeess',
                                                  'eemmm', 'eemmo', 'eemms', 'eemoo', 'eemos',
                                                  'eemss', 'eeooo', 'eeoos', 'eeoss', 'eesss',
                                                  'emmmm', 'emmmo', 'emmms', 'emmoo', 'emmos',
                                                  'emmss', 'emooo', 'emoos', 'emoss', 'emsss',
                                                  'eoooo', 'eooos', 'eooss', 'eosss', 'essss',
                                                  'mmmmm', 'mmmmo', 'mmmms', 'mmmoo', 'mmmos',
                                                  'mmmss', 'mmooo', 'mmoos', 'mmoss', 'mmsss',
                                                  'moooo', 'mooos', 'mooss', 'mosss', 'mssss',
                                                  'ooooo', 'oooos', 'oooss', 'oosss', 'ossss', 'sssss']


if __name__ == "__main__":
    test_get_combinations_with_r()
