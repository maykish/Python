#!/usr/bin/python3

num = [1, 2, 3, 4, 5]

f = 0
l = len(num) - 1

while l - f > 1:
    #switch
    num[f], num[l] = num[l], num[f]

    f += 1
    l -= 1

print(num)



