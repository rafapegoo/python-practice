"""
Basic Sum Calculator

Task:
Takes two integer inputs from the user and displays their sum in a formatted message.

Example Usage:
Input:
Digite um valor: 5
Digite outro valor: 3
Output:
A soma entre 5 e 3 é igual a 8

Key Concepts Demonstrated:
- User input handling with input()
- Type conversion (string to integer)
- Variable assignment and arithmetic operations
- String formatting with .format() method
- Basic program structure in Python

Note: This exercise demonstrates fundamental Python operations for beginners.
"""

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
print ('A soma entre {} e {} é igual a {}'.format(n1,n2,s))
