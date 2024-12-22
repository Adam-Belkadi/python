total_amount = int(input("Total amount: "))
number_items = int(input("Number of items: "))
current_day = input("Day of the week: ").lower()

discount = 0
if number_items > 5: discount += 5

if current_day == "monday" or current_day == "friday":
    discount += 10
else:
    discount += 20

new_price = total_amount - (total_amount * discount / 100)

print(f"Total price after {discount}% discount: {new_price} dinars")
