'''Task: Runner-Up Score

Given a list of scores, find the second highest (runner-up) score.

Input:
- Integer n (number of scores)
- List of n integers (the scores)

Output:
- Integer (runner-up score)

Example:
5
2 3 6 6 5
→ 5

Explanation:
Unique scores: [2, 3, 5, 6]
Highest is 6, runner-up is 5.'''


if __name__ == '__main__':
    n = int(input()) #Reads the number of elements (5)
    arr = list(map(int, input().split())) # Reads the numbers: [2, 3, 6, 6, 5]
    unique_scores = sorted(set(arr), reverse=True)# Removes duplicates and sorts in descending order: [6, 5, 3, 2]
    print (unique_scores[1]) # Prints the second highest score (5)