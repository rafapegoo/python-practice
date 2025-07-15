"""
Safe Division Calculator

Task:
Perform and display both integer and floating-point division of two numbers,
with protection against division by zero.

Features:
- Input validation for division by zero
- Demonstrates both floor division (//) and true division (/)
- Clean output of results

Example Usage:
Input: 
7
2
Output:
3 (integer division)
3.5 (float division)

Error Case:
Input:
5
0
Output:
"Error: division by zero is not allowed"

Key Concepts:
- Basic input handling
- Error prevention
- Different division operations in Python
- Conditional logic
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if b == 0:
        print('Error: division by zero is not allowed')
    else:
        int_div = a // b 
        flo_div = a / b
        
        print (int_div)
        print (flo_div)
