#!/usr/bin/python3
# Performs binary search on the dataset provided by "download_IMDb.py",
# searching for a name in the huge list of names cut out from the database.

def fetch_sorted_names():
    f = open("sorted_names.txt", "r")

    return f.read().split("\n")

def binary_search(elements, value):
    print(f"\nIs the name \"{value}\" in the list of IMDb's names?")
    
    def recursive(left, right):
        if left <= right:
            middle = (left + right) // 2

            if elements[middle] == value:
                return True
            if elements[middle] < value:
                return recursive(middle + 1, right)
            if elements[middle] > value:
                return recursive(left, middle - 1)

        return False
    return recursive(0, len(elements) - 1)

sorted_names = fetch_sorted_names()
print(binary_search(sorted_names, "John Smith")) # Searching for name John Smith
