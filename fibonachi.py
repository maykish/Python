#!/usr/bin/python3

num_before_last = 0
last_num = 1

print(num_before_last)

while last_num <= 50:
    print(last_num)
    
    last_num = num_before_last + last_num
    num_before_last = last_num - num_before_last
    

    
