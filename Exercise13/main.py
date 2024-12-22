while True:
    user_input = input("Please type in a string: ")
    if not user_input:
        break
    print(user_input)
    print("-" * len(user_input))