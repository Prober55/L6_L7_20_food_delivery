# L6_L7_20_food_delivery — Food Delivery

## Lab 7: Fuzz Testing for Input Validation Bugs

### Student Details
- **Name:** John S Thomas
- **SRN:** PES2UG24CS207

---

### Files

| File | Description |
|------|-------------|
| [`food_delivery.py`](food_delivery.py) | Application script hardened against malformed and unexpected inputs |
| [`test_food_delivery.py`](test_food_delivery.py) | Property-based fuzz testing suite using Hypothesis |
| [`PES2UG24CS207_John_S_Thomas_Lab7.pdf`](PES2UG24CS207_John_S_Thomas_Lab7.pdf) | Lab report with screenshots of execution and test results |

---

### Edge Cases Uncovered via Fuzz Testing

1. **`parse_order(items_csv)`**:
   - `None` input raised `AttributeError: 'NoneType' object has no attribute 'split'`.
   - Empty string `""` or entries without `:` raised `ValueError: not enough values to unpack (expected 2, got 1)`.
   - Missing/non-integer quantity like `":"` or `"pizza:abc"` raised `ValueError: invalid literal for int() with base 10: ''`.
   - **Fix:** Added type checking, empty string guarding, format validation, positive integer checks, and safe fallback returning `{}`.

2. **`delivery_eta(distance_km)`**:
   - `None` input raised `TypeError: float() argument must be a string or a real number, not 'NoneType'`.
   - Empty or non-numeric strings raised `ValueError: could not convert string to float: ''`.
   - Negative values, `NaN`, or `Infinity` produced erroneous results.
   - **Fix:** Validated numeric conversions, guarded against negative distances and non-finite floats, returning safe default ETA `0`.

3. **`coupon_discount(code)`**:
   - `None` input raised `AttributeError: 'NoneType' object has no attribute 'upper'`.
   - Strings without `"SAVE"` raised `IndexError: list index out of range`.
   - `"SAVE"` with no digits or non-numeric suffixes raised `ValueError: invalid literal for int() with base 10: ''`.
   - **Fix:** Validated string types, extracted discount digits via regex pattern `SAVE\s*(\d+)`, returning `0` for invalid/missing codes.

---

### How to Run

1. **Activate virtual environment:**
   ```bash
   source ../.venv/bin/activate
   ```

2. **Run the application:**
   ```bash
   python food_delivery.py
   ```

3. **Run the Hypothesis fuzz tests:**
   ```bash
   pytest test_food_delivery.py
   ```
