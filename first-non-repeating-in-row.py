#!/usr/bin/python3
# Return the first element that is not repeating in a row
s = "sssssuiiioopp"
answer = -1

print(f"string = {s}")

for index in range(len(s) - 1):
    if s[index] != s[index + 1]:
        if index == 0:
            answer = index
            break
        elif s[index] != s[index - 1]:
            answer = index
            break
    
                
print(f"last_element = {s[answer]}, index = {answer}")
