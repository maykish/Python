#!/usr/bin/env python3

# This sort works by comparing each element to pivot (always last element of arr)  

def partition(arr):
    pivot = 0
    L = 1
    R = len(arr) - 1
   
    while R - L != 1:
        while arr[L] < arr[pivot]:
            L += 1
        while arr[R] > arr[pivot]:
            R -= 1
        
        arr[L], arr[R] = arr[R], arr[L]
    
    return L #border

nums = [45, 10, 99, 80, 13, 23, 12, 15, 16, 1, 93, 3, 40, 58, 11, 100, 30, 25, 60, 70, 85, 25]
print(f"\nbefore partition:\n{nums}")
print("border index = ", partition(nums))
print(f"after partition:\n{nums}")
