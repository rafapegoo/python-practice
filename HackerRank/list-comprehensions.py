"""
3D Coordinate Generator with List Comprehensions

Task:
Given three integers (x, y, z) representing cuboid dimensions and an integer n, generate all possible 3D coordinates (i, j, k) where:
- 0 ≤ i ≤ x
- 0 ≤ j ≤ y
- 0 ≤ k ≤ z
- i + j + k ≠ n

The solution must use list comprehensions and return the results in lexicographic order.

Example Usage:
Input:
1
1
1
2
Output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Key Concepts Demonstrated:
- List comprehensions for concise iteration
- Multiple loop variables in comprehensions
- Conditional filtering in comprehensions
- Generating Cartesian products
- Lexicographic ordering of results

Note: This exercise focuses on advanced list comprehension techniques in Python.
"""

if __name__ == '__main__': #runs the main code
    x = int(input()) #read the x value 
    y = int(input()) # reads the y value
    z = int(input()) # reads the z value
    n = int(input()) # reads the n valu
    
lista = [ [i, j, k] #create a list of lists
          for i in range(x + 1) # i goes from 0 up to x
          for j in range(y + 1) # j goes from 0 up to y
          for k in range(z + 1)# k goes from 0 up to z
          if i + j + k != n ]  # only includes if the sum is different from n
print(lista) # prints the final result