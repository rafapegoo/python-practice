"""
Square Root Calculator with Round Up

Task:
Calculate the square root of a user-provided number and display the result rounded up to the nearest integer.

Example:
Input: Enter a number: 5.3
Output: The square root of 5.3 is equal to 3

Key Concepts Demonstrated:
- Math module usage (math.sqrt, math.ceil)
- Float input handling
- String formatting with .format()
- Basic console I/O operations

Note: This was one of my early Python exercises while learning fundamental math operations.
"""

import math
num = float(input('Digite um número:'))
raiz = math.sqrt(num)
print ('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
