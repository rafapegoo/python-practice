"""
Task: 
Given an integer 'n', print the square of all non-negative integers less than 'n' in ascending order, each on a new line.

Example Input/Output:
Input: 5
Output:
0
1
4
9
16

Key Concepts Demonstrated:
- User input handling
- For loops with range()
- Mathematical operations
- Basic Python syntax and structure

Note: This solution was developed as part of learning Python fundamentals.
"""
if __name__ == '__main__':
    n = int(input())
    i = 0
    
    for i in range(n):
        print(i * i)
