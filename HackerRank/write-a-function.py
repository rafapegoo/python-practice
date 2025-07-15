"""
Task: Leap Year Checker
Given a year, determine if it is a leap year. Return True if it is, otherwise False.

Leap Year Rules:
1. If the year is divisible by 400 → Leap year (True)
2. Else, if divisible by 100 → Not leap year (False)
3. Else, if divisible by 4 → Leap year (True)
4. Otherwise → Not leap year (False)

Input: Integer (year)
Output: Boolean (True/False)

Example:
1990 → False (not divisible by 4)
2000 → True (divisible by 400)
2024 → True (divisible by 4, not by 100)
"""

def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap

year = int(input())
