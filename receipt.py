
item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075" # 7.5%  sales tax

price1 = float(item1_price)
quantity1 = int(item1_qty)
tax1 = float(tax_rate)

price2 = float(item2_price)
quantity2 = int(item2_qty)
tax2 = float(tax_rate)

price3 = float(item3_price)
quantity3 = int(item3_qty)
tax3 = float(tax_rate)

subtotal1 = price1 * quantity1
tax_rate1 = subtotal1 * tax1
total1 = subtotal1 * tax_rate1

subtotal2 = price2 * quantity2
tax_rate2 = subtotal2 * tax2
total2 = subtotal2 *tax_rate2

subtotal3 = price3 * quantity3
tax_rate3 = subtotal3 * tax3
total3 = subtotal3 * tax_rate3

print("=" * 40)
print("STORE RECEIPT")
print("=" * 40)

print(f"Product: {item1_name}")
print(f"Price: ${item1_price} * {item1_qty}")
print(f"Subtotal: {subtotal1}")
print(f"Tax: ({tax_rate1 * 100}%): ${tax1}")
print(f"Total: ${total1}")

print(f"Product: {item2_name}")
print(f"Price: ${item2_price} * {item2_qty}")
print(f"Subtotal: {subtotal2}")
print(f"Tax: ({tax_rate2 * 100}%): ${tax2}")
print(f"Total: ${total2}")

print(f"Product: {item3_name}")
print(f"Price: ${item3_price} * {item3_qty}")
print(f"Subtotal: {subtotal3}")
print(f"Tax: ({tax_rate3 * 100})% {tax3}")
print(f"Total: ${total3}")
