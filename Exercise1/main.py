TICKET_PRICE = 15.50
name = input("Please enter your name:")

if name.lower() == "vip":
    print("Enjoy the show for free!")
else:
    tickets_nb = int(input("How many tickets would you like to buy?"))
    print(f"The total cost is ${tickets_nb * TICKET_PRICE}")
    print("Enjoy your tickets!")
