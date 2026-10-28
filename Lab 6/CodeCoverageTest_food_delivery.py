import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


class TestCodeCoverageFoodDelivery:
    """Test suite designed to achieve full code (statement/line) coverage."""

    # --- delivery_charge line coverage tests ---
    def test_delivery_charge_out_of_range(self):
        with pytest.raises(ValueError, match="out of delivery range"):
            delivery_charge(0, 200, False)

    def test_delivery_charge_free_delivery(self):
        assert delivery_charge(5, 500, False) == 0

    def test_delivery_charge_short_distance(self):
        assert delivery_charge(2, 200, False) == 20

    def test_delivery_charge_medium_distance(self):
        assert delivery_charge(6, 200, False) == 40

    def test_delivery_charge_long_distance(self):
        assert delivery_charge(10, 200, False) == 60

    def test_delivery_charge_with_rain(self):
        assert delivery_charge(2, 200, True) == 50

    # --- apply_coupon line coverage tests ---
    def test_apply_coupon_none(self):
        assert apply_coupon(300, None, False) == 300

    def test_apply_coupon_invalid(self):
        with pytest.raises(ValueError, match="invalid coupon"):
            apply_coupon(300, "INVALID", False)

    def test_apply_coupon_welcome_not_first_order(self):
        with pytest.raises(ValueError, match="coupon only for first order"):
            apply_coupon(300, "WELCOME", False)

    def test_apply_coupon_order_below_minimum(self):
        assert apply_coupon(150, "SAVE50", False) == 150

    def test_apply_coupon_save50_success(self):
        assert apply_coupon(300, "SAVE50", False) == 250

    # --- estimated_time line coverage test ---
    def test_estimated_time_peak_and_busy(self):
        # Triggers all lines 33-40 in estimated_time
        # (15 + 2*4) + 10 (peak) + 15 (busy) + 5 (nested peak) = 53
        assert estimated_time(2, True, True) == 53
