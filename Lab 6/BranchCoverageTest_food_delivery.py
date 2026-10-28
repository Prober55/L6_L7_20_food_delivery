import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


class TestBranchCoverageFoodDelivery:
    """Comprehensive branch coverage test suite covering all decision branches."""

    # ==========================================
    # 1. delivery_charge branch coverage
    # ==========================================
    def test_delivery_charge_distance_le_zero(self):
        # Branch: distance_km <= 0 (True)
        with pytest.raises(ValueError, match="out of delivery range"):
            delivery_charge(0, 250, False)
        with pytest.raises(ValueError, match="out of delivery range"):
            delivery_charge(-3, 250, False)

    def test_delivery_charge_distance_gt_15(self):
        # Branch: distance_km <= 0 (False), distance_km > 15 (True)
        with pytest.raises(ValueError, match="out of delivery range"):
            delivery_charge(15.5, 250, False)

    def test_delivery_charge_free_delivery_no_rain(self):
        # Branches: order_value >= 500 (True), is_raining (False)
        assert delivery_charge(5, 500, False) == 0

    def test_delivery_charge_free_delivery_with_rain(self):
        # Branches: order_value >= 500 (True), is_raining (True)
        assert delivery_charge(5, 700, True) == 30

    def test_delivery_charge_tier_le_3_no_rain(self):
        # Branches: order_value >= 500 (False), distance_km <= 3 (True), is_raining (False)
        assert delivery_charge(3, 250, False) == 20

    def test_delivery_charge_tier_le_3_with_rain(self):
        # Branches: order_value >= 500 (False), distance_km <= 3 (True), is_raining (True)
        assert delivery_charge(1, 250, True) == 50

    def test_delivery_charge_tier_le_8_no_rain(self):
        # Branches: distance_km <= 3 (False), distance_km <= 8 (True), is_raining (False)
        assert delivery_charge(8, 250, False) == 40

    def test_delivery_charge_tier_le_8_with_rain(self):
        # Branches: distance_km <= 3 (False), distance_km <= 8 (True), is_raining (True)
        assert delivery_charge(5, 250, True) == 70

    def test_delivery_charge_tier_gt_8_no_rain(self):
        # Branches: distance_km <= 8 (False) -> else, is_raining (False)
        assert delivery_charge(12, 250, False) == 60

    def test_delivery_charge_tier_gt_8_with_rain(self):
        # Branches: distance_km <= 8 (False) -> else, is_raining (True)
        assert delivery_charge(15, 250, True) == 90

    # ==========================================
    # 2. apply_coupon branch coverage
    # ==========================================
    def test_apply_coupon_none(self):
        # Branch: code is None (True)
        assert apply_coupon(350, None, False) == 350

    def test_apply_coupon_invalid_code(self):
        # Branch: code is None (False), code not in COUPONS (True)
        with pytest.raises(ValueError, match="invalid coupon"):
            apply_coupon(300, "DISCOUNT50", False)

    def test_apply_coupon_welcome_not_first_order(self):
        # Branch: code == "WELCOME" (True) and not is_first_order (True)
        with pytest.raises(ValueError, match="coupon only for first order"):
            apply_coupon(300, "WELCOME", False)

    def test_apply_coupon_welcome_valid_first_order(self):
        # Branch: code == "WELCOME" (True) and not is_first_order (False), order_value >= 200
        assert apply_coupon(300, "WELCOME", True) == 200

    def test_apply_coupon_welcome_under_min_order_value(self):
        # Branch: code == "WELCOME" (True), not is_first_order (False), order_value < 200 (True)
        assert apply_coupon(150, "WELCOME", True) == 150

    def test_apply_coupon_save50_under_min_order_value(self):
        # Branch: code == "SAVE50" (code == "WELCOME" is False), order_value < 200 (True)
        assert apply_coupon(199, "SAVE50", False) == 199

    def test_apply_coupon_save50_valid_order(self):
        # Branch: code == "SAVE50" (code == "WELCOME" is False), order_value < 200 (False)
        assert apply_coupon(200, "SAVE50", False) == 150
        assert apply_coupon(500, "SAVE50", True) == 450

    # ==========================================
    # 3. estimated_time branch coverage (All 4 boolean paths)
    # ==========================================
    def test_estimated_time_normal_conditions(self):
        # Branches: is_peak_hour=False, restaurant_busy=False
        # minutes = 15 + 4 * 5 = 35
        assert estimated_time(5, is_peak_hour=False, restaurant_busy=False) == 35

    def test_estimated_time_peak_hour_only(self):
        # Branches: is_peak_hour=True, restaurant_busy=False
        # minutes = 15 + 4 * 5 + 10 = 45
        assert estimated_time(5, is_peak_hour=True, restaurant_busy=False) == 45

    def test_estimated_time_restaurant_busy_only(self):
        # Branches: is_peak_hour=False, restaurant_busy=True (nested is_peak_hour=False)
        # minutes = 15 + 4 * 5 + 15 = 50
        assert estimated_time(5, is_peak_hour=False, restaurant_busy=True) == 50

    def test_estimated_time_peak_and_busy(self):
        # Branches: is_peak_hour=True, restaurant_busy=True (nested is_peak_hour=True)
        # minutes = 15 + 4 * 5 + 10 + 15 + 5 = 65
        assert estimated_time(5, is_peak_hour=True, restaurant_busy=True) == 65
