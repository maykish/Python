#!/usr/bin/python3

s = input()

words = s.replace(".", "").replace(",","").replace("...", " ").split(" ")
sum = 0

for word in words:
    sum += len(word)
    
average = sum/len(words)
print(f"average word length = {average}")
