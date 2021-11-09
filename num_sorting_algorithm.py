#!/bin/usr/python3
# This program sorts a given number sequence into an 
# order from integers, small to large.

def bubbleSort(numbers):
    has_swapped = True
    num_of_iterations = 0 

    while(has_swapped): # Stops running cycle if no swaps were made in previous iteration
        has_swapped = False
        for index in (range(len(numbers) - num_of_iterations - 1)): # Decreases amount of sorting after each cycle
            if numbers[index] >= numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index] # Swap
                has_swapped = True

        num_of_iterations += 1
    
    return numbers

numbers_to_sort = [4, 1, 3, 10, 5]
bubbleSort(numbers_to_sort)
print(numbers_to_sort)


