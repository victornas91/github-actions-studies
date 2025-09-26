from src import calc


def test_sum():
    assert calc.sum(2, 3) == 5
    assert calc.sum(-1, 1) == 0


def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 4) == -4
