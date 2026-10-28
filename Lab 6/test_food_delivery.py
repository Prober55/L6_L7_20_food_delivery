import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time

# Initial example test cases:
def test_nearby_small_order():
    assert delivery_charge(2, 200, False) == 20

def test_no_coupon():
    assert apply_coupon(300, None, False) == 300

# Full test cases achieving 100% code and branch coverage:

# --- delivery_charge tests ---
def test_delivery_charge_out_of_range_low():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)

def test_delivery_charge_out_of_range_high():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(15.1, 200, False)

def test_delivery_charge_free_delivery():
    assert delivery_charge(5, 500, False) == 0

def test_delivery_charge_free_delivery_with_rain():
    assert delivery_charge(5, 600, True) == 30

def test_delivery_charge_medium_distance():
    assert delivery_charge(5, 200, False) == 40

def test_delivery_charge_medium_distance_rain():
    assert delivery_charge(8, 200, True) == 70

def test_delivery_charge_long_distance():
    assert delivery_charge(10, 200, False) == 60

def test_delivery_charge_long_distance_rain():
    assert delivery_charge(15, 200, True) == 90

# --- apply_coupon tests ---
def test_apply_coupon_invalid():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "INVALID", False)

def test_apply_coupon_welcome_not_first_order():
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)

def test_apply_coupon_welcome_valid_first_order():
    assert apply_coupon(300, "WELCOME", True) == 200

def test_apply_coupon_welcome_under_min_order():
    assert apply_coupon(150, "WELCOME", True) == 150

def test_apply_coupon_save50_under_min_order():
    assert apply_coupon(150, "SAVE50", False) == 150

def test_apply_coupon_save50_valid_order():
    assert apply_coupon(300, "SAVE50", False) == 250

# --- estimated_time tests (all 4 branch paths) ---
def test_estimated_time_offpeak_not_busy():
    assert estimated_time(5, False, False) == 35

def test_estimated_time_peak_not_busy():
    assert estimated_time(5, True, False) == 45

def test_estimated_time_offpeak_busy():
    assert estimated_time(5, False, True) == 50

def test_estimated_time_peak_busy():
    assert estimated_time(5, True, True) == 65
