order_lines = [
{'description': 'SET-KASTRON SPLIT 2 TON', 'quantity': 2, 'unit_price': 180, 'tax_percentage': 0.1, 'subtotal': 360, 'total': 396},
{'description': 'SET-KASTRON AQUACHILL 1.5 TON', 'quantity': 1, 'unit_price': 200, 'tax_percentage': 0.1, 'subtotal': 200, 'total': 220},
{'description': 'SAMSUNG 43" CU-7000', 'quantity': 1, 'unit_price': 119, 'tax_percentage': 0.1, 'subtotal': 119, 'total': 130.9},
]

discounts = [10, 5, 1]

print("Data Before Discount")
for index in range(len(order_lines)):
    print(f"{order_lines[index]} : Discount {discounts[index]}BD")

def apply_discounts(order_lines, discounts):
    for i, order in enumerate(order_lines):
        order['discount'] = discounts[i]
        new_subtotal = order['subtotal'] - order['discount']
        new_total = new_subtotal + (new_subtotal * order['tax_percentage'])
        order['subtotal'] = new_subtotal
        order['total'] = new_total

apply_discounts(order_lines, discounts)

print("Data After Discount")
for order in order_lines:
    print(order)
