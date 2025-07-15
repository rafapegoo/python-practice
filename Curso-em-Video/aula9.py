"""
String Splitting and Indexing Exercise

Task:
Demonstrate string manipulation by:
1. Splitting a sentence into words
2. Accessing specific characters from selected words

Example:
Input: "curso em video Python"
Output: 'e' (3rd letter from 3rd word)

Key Concepts Demonstrated:
- String splitting with .split()
- List indexing (accessing elements by position)
- Nested indexing (accessing characters in strings within lists)
- Zero-based indexing in Python

Breakdown:
1. frase.split() → ["curso", "em", "video", "Python"]
2. dividido[2] → "video"
3. dividido[2][3] → 'e' (4th character of "video")

Note: This exercise helps understand Python's string and list indexing systems.
"""

frase = "curso em video Python"
dividido = (frase.split())
print(dividido[2][3])
