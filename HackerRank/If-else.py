#!/bin/python3
"""
Task:
Determine if a given integer is 'Weird' or 'Not Weird' based on:
- Odd numbers are Weird
- Even numbers in range 2-5: Not Weird
- Even numbers in range 6-20: Weird
- Even numbers >20: Not Weird

Example Input/Output:
Input: 3 → Output: Weird
Input: 24 → Output: Not Weird

Key Concepts Demonstrated:
- Conditional logic (if/elif/else)
- Modulo operations (%)
- Range comparisons
- Basic Python I/O operations

Note: Solution for HackerRank's 'Python If-Else' problem (30 Days of Code)
"""

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird')
    elif 2 <= n <= 5:
        print('Not Weird')
    elif 6 <= n <= 20: 
        print('Weird')
    else: 
        print('Not Weird')
