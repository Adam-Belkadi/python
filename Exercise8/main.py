number = int(input("Number: "))

output = ""

if number % 3 == 0: output += "Fizz"
if number % 5 == 0: output += "Buzz"

print(output)