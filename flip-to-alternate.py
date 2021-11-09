#!/usr/bin/python3

arr = [1, 1, 0, 1, 1]

def flip_y(arr):
    print("N")
    if arr[0] == arr[1]:
        if arr[0] == 1:
            arr[1] = 0
        if arr[0] == 0:
            arr[1] = 1
        print("H")
        flip(arr[1:])
   
def flip_x(arr):
    if len(arr) < 2:
        return 0
    else:
        if arr[0] == arr[1]:
            if arr[0] == 1:
                arr[0] = 0
            if arr[0] == 0:
                arr[0] = 1
            flip(arr[1:])

def flip(arr):
    flips = 1
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            flips += 1
            if arr[i] == 1:
                arr[i + 1] = 0
            if arr[i] == 0:
                arr[i + 1] = 1

    return flips

def main(arr):
    print(arr, flip_y(arr))
    print(arr, flip_x(arr))

    #if x < y:
    #    return x
    #else:
    #    return x


#print(arr, main(arr))
            

