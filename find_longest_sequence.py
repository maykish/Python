#!/usr/bin/python

n = [0, 10]  

def find_longest_sequence(arr):
    longest_sequence_index = 0
    longest_sequence_length = 1
    current_sequence_length = 1

    for index in range(len(arr) - 1):
        if arr[index] == arr[index + 1]:
            current_sequence_length += 1
            
            if current_sequence_length > longest_sequence_length: 
                longest_sequence_index = index - current_sequence_length + 2
                longest_sequence_length = current_sequence_length
        else: 
            current_sequence_length = 1

    return longest_sequence_length, longest_sequence_index, arr[longest_sequence_index]
        

print(f"array = {n}")
print(find_longest_sequence(n))
