#!/usr/bin/env python3

# Sorts an array by starting with second element, and with each chosen element it compares it to all the elements beforehand,
# finding when it is bigger than the element before it or has nothing to compare to, and inserting it in its proper place. 
# Repeats until finishes sorting the final value.

def insertion_sort(array):
    for a in range(1,len(array)): # Selects index of element
        print(numbers)
        for b in reversed(range(a)): # Selects indexes of elements to compare to in reverse    
              if array[b] > array[b + 1]:
                    array[b], array[b + 1] = array[b + 1], array[b] 

numbers = [5, 1, 6, 2, 4, 3]
insertion_sort(numbers)
#print(numbers)
