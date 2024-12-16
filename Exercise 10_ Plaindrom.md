### **Exercise: Palindrome Checker**

**Objective**: Write a program that checks whether a word is a palindrome, using negative indexing and loops.

### **Task**:
1. **Input**:
   - Ask the user to type in a word.
2. **Loop through the first half of the word**:
   - Compare each character in the word from the start and the end using negative indexing.
   - If at any point the characters do not match, the word is not a palindrome.
3. **Output**:
   - After the loop, print `Yes, it's a palindrome.` if all characters match.
   - If any characters do not match, print `No, it's not a palindrome.`

### **Steps**:
1. **Request Input**: 
   - Prompt the user to type a word.
2. **Check for Palindrome**:
   - Use a loop to compare characters from the beginning and end of the string.
   - If any characters don't match, set a variable `is_palindrome` to `False` and stop the loop.
3. **Output the Result**:
   - After finishing the loop, print the result based on whether `is_palindrome` is `True` or `False`.

### **Example**:

1. **Input**: 
   ```
   racecar
   ```
   **Output**:
   ```
   Yes, it's a palindrome.
   ```

2. **Input**: 
   ```
   hello
   ```
   **Output**:
   ```
   No, it's not a palindrome.
   ```

---

**Bonus**: Try testing the program with multiple words and phrases.