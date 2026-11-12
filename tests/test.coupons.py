import pytest
from pricing import apply_coupon


def test_coupon_welcome10():
    assert apply_coupon(100,"welcome10") == 90


def test_coupon_vip20_lowercase():
    assert apply_coupon(100,"vip20") == 80


def test_coupon_unknown_raises():
    with pytest.raises(ValueError): 
        apply_coupon(100,"INVALID50")
