from src.calc import sum, subtract


def test_sum():

    assert sum(2, 3) == 5

    assert sum(-1, 1) == 0

def test_subtract():

    assert subtract(5, 3) == 2

    assert subtract(0, 4) == -4


