with open("test_write.txt", "w") as text:
    text.write("Hello")

with open("test_append", "a") as text_append:
    text_append.write("Hello\n")
