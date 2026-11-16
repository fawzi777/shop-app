from pricing import loyalty_points


def test_loyalty_points_high():
    assert loyalty_points(600) == 60


def test_loyalty_points_medium():
    assert loyalty_points(200) == 20


def test_loyalty_points_low():
    assert loyalty_points(50) == 0
