age1 = int(input("Please type in the age of the first person: "))
age2 = int(input("Please type in the age of the first person: "))

if age1 == age2 :
    print("Both people are the same age!")
elif age1 > age2:
    print(f"The older age is: {age1}")
else:
    print(f"The older age is: {age2}")
