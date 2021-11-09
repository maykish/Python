#!/usr/bin/python3

numbers = -497

print("before: %d" % numbers)

if "-" in str(numbers):
    numbers = "-" + str(numbers)[1:][::-1]
else:
    numbers = str(numbers)[::-1]

print("after: %s" % numbers)



