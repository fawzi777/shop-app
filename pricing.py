"""Price helpers for Shop App. All prices are in ILS."""

VAT_RATE = 0.18


def apply_discount(price, percent):
    """Return the price after a percent discount."""
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (100 - percent) / 100, 2)


def add_vat(price, rate=VAT_RATE):
    """Return the price with VAT added."""
    return round(price * (1 + rate), 2)


def cart_total(prices):
    """Return the sum of all prices in the cart."""
    return round(sum(prices), 2)


def apply_coupon(price, code):
    """return the price after applying a valid coupone code."""
    coupons = {
        "WELCOME10": 10,
        "VIP20": 20,
    }
    normalized = code.strip().upper()
    if normalized not in coupons:
        raise ValueError(f"Unknown coupon code: {code}")
    return apply_discount(price, coupons[normalized])
