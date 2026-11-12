from pricing import shipping_cost


def test_shipping_free_at_200():
    assert shipping_cost(200) == 0


def test_shipping_midrange_from_100_to_199():
    assert shipping_cost(150) == 15


def test_shipping_under_100():
    assert shipping_cost(50) == 30
