"""
Number Successor and Predecessor Calculator

Task:
For a given integer, calculate and display both its immediate successor (n+1) 
and predecessor (n-1), demonstrating two different implementation approaches.

Approaches Demonstrated:
1. Variable storage method (stores results before printing)
2. Direct calculation method (calculates during printing)

Example Output:
Input: 5
Output: "O sucessor de 5 é 6 e seu antecessor é 4"

Key Concepts:
- Basic arithmetic operations
- Variable assignment vs direct calculation
- String formatting with .format()
- User input handling
"""

n = int(input('Digite um numero:'))
s = n + 1
a = n - 1
print ('O sucessor de {} é {} e seu antecessor é {}'.format(n, s, a))

n = int(input('Digite um numero:'))
print ('O sucessor de {} é {} e seu antecessor é {}'.format(n, (n+1),(n-1)))


