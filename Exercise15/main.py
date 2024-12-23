word = input("Please type in a string: ").lower()

a_found = False
e_found = False
o_found = False

for char in word:
    if not a_found and char == 'a':
        a_found = True
    if not e_found and char == 'e':
        e_found = True
    if not o_found and char == 'o':
        o_found = True

if a_found:
    print("a found")
else:
    print("a not found")
if e_found:
    print("e found")
else:
    print("e not found")
if o_found:
    print("o found")
else:
    print("o not found")
