#!/usr/bin/python3

import math 

def get_roots(a, b, c):
    root_calc = int(math.sqrt(b**2 - 4*a*c))
    divident_x = b*-1 + root_calc
    divident_y = b*-1 - root_calc

    return {int(divident_x/(a*2)), int(divident_y/(a*2))}

print(get_roots(1, 5, 6))


