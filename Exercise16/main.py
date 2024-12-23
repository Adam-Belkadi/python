numbers = [1, 2, 3, 4, 5]

while True:
    index = input("Enter index (-1 to quit): ")

    if not index.isdigit() and index != "-1":
        print("Invalid input. Please enter an integer.")
        continue
    index = int(index)

    if index == -1:
        print("Exiting the program.")
        break

    if index < 0 or index >= len(numbers):
        print(f"Invalid index. Please enter a number between 0 and {len(numbers) - 1}.")
        continue

    new_value = input("Enter new value: ")
    if not new_value.isdigit():
        print("Invalid input. Please enter an integer.")
        continue

    new_value = int(new_value)


    numbers[index] = int(new_value)

print(numbers)