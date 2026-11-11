import math
import re

def parse_order(items_csv):
    order = {}
    if not items_csv or not isinstance(items_csv, str):
        return order
    for item in items_csv.split(','):
        item = item.strip()
        if not item or ':' not in item:
            continue
        parts = item.split(':')
        if len(parts) != 2:
            continue
        name, qty_str = parts[0].strip(), parts[1].strip()
        if not name:
            continue
        try:
            qty = int(qty_str)
            if qty > 0:
                order[name] = qty
        except (ValueError, TypeError):
            continue
    return order

def delivery_eta(distance_km):
    if distance_km is None:
        return 0
    try:
        dist = float(distance_km)
        if dist < 0 or math.isnan(dist) or math.isinf(dist):
            return 0
        return int(15 + dist * 4)
    except (ValueError, TypeError, OverflowError):
        return 0

def coupon_discount(code):
    if not code or not isinstance(code, str):
        return 0
    code_upper = code.upper().strip()
    match = re.search(r'SAVE\s*(\d+)', code_upper)
    if match:
        try:
            return int(match.group(1))
        except (ValueError, OverflowError):
            return 0
    return 0

def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    result = parse_order(user_input)
    print("Order:", result)

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    result = delivery_eta(user_input)
    print("ETA in Minutes:", result)

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    result = coupon_discount(user_input)
    print("Discount:", result)

if __name__ == "__main__":
    main()
