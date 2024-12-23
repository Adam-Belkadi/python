word = input("Input a word: ")

frame_width = 30

word_len = len(word)
left_padding = (frame_width - word_len) // 2
right_padding = frame_width - word_len - left_padding

print("*" * frame_width)
print("*" + " " * (left_padding - 1) + word + " " * (right_padding - 1) + "*")
print("*" * frame_width)