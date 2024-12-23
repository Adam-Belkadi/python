numbers = []
shoe_sizes = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)

combined_list = numbers + shoe_sizes

print("Numbers list:", numbers)
print("Shoe sizes list:", shoe_sizes)
print("Combined numbers and shoe sizes list:", combined_list)