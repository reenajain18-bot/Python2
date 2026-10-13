
# ================================
# GROCERY BILLING QUEUE
# ================================

print("=== Grocery Billing Queue ===\n")

# PART 1: Initialize the counters
low_price_items = 0
medium_price_items = 0
high_price_items = 0

customers_served = 0
total_sales = 0

billing = True

# PART 2: Outer while loop - one customer per repeat
while billing:

    customer_name = input("Enter customer name: ")
    item_count = int(input("How many items are you buying? "))

    # PART 3: Check for an invalid item count
    if item_count <= 0:
        print("Invalid item count. Please try again.\n")
        continue

    # PART 4: Inner while loop - one item per repeat
    customer_total = 0
    item_number = 1

    while item_number <= item_count:

        item_name = input("Enter item name: ")
        price = int(input("Enter price per item: "))
        quantity = int(input("Enter quantity: "))

        # PART 5: Validate price and quantity
        if price <= 0 or quantity <= 0:
            print("Price and quantity must be greater than zero.")
            print("Please enter the item details again.\n")
            continue

        # Calculate the item total
        item_total = price * quantity

        print(
            item_name, ":", quantity, "x", price,
            "=", item_total
        )

        customer_total += item_total

        # Count items according to their price
        if price < 50:
            low_price_items += quantity
        elif price <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity

        # Move to the next item
        item_number += 1

    # PART 6: Finish billing for the customer
    customers_served += 1
    total_sales += customer_total

    print("\nCustomer:", customer_name)
    print("Customer's total bill: Rs.", customer_total)

    next_customer = input(
        "\nNext customer? (yes/no): "
    ).lower()

    if next_customer != "yes":
        billing = False

# PART 7: Print the nested for-loop report
print("\n===== GROCERY SALES REPORT =====")

price_bands = [
    ("Low-price items", low_price_items),
    ("Medium-price items", medium_price_items),
    ("High-price items", high_price_items)
]

for band_name, count in price_bands:
    print(band_name + ": ", end="")

    for i in range(count):
        print("*", end="")

    print()

print("\nCustomers served:", customers_served)
print("Total sales: Rs.", total_sales)
print("================================")
