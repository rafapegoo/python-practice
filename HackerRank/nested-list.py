"""
Given students' names and grades, print names with the second lowest grade.
If multiple students match, sort names alphabetically.
  
Input:
- First line: N (number of students)
- Next 2N lines: name followed by grade
  
Output:
- Names with second lowest grade (one per line, alphabetized)
  
Example:
5
Harry 37.21 → Berry
Berry 37.21 → Harry
Tina 37.2
Akriti 41
Harsh 39
"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    scores = [score for name, score in students]
    
    unique_scores = sorted(set(scores))
    
    second_lowest = unique_scores[1]
    
    names = sorted([name for name, score in students if score 
    == second_lowest])
    
    for names in names:
        print (names)