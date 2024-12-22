word = input("Type a word: ")
is_palindrome = True
i = 0

while is_palindrome and i < int(len(word) / 2):
    if word[i] != word[-(i+1)]:
        is_palindrome = False
    i+=1

if i == int(len(word) / 2):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palidrome")
print(f"{i}  {len(word) / 2}")