#!/usr/bin/python3
# Return the index of the first non repeating element in a string.

text = "aappr"
answer = -1

for index in range(len(text)):
    if text[index] not in text[:index] + text[index + 1:]:
        answer = index
        break

print(f"text = {text}, index = {answer}")
