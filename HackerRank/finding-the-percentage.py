"""
Task: Student Average Marks Calculator

Given a dictionary of student names and their marks, calculate the average marks 
for a specific student and format it to 2 decimal places.

Input:
- First line: integer n (number of students)
- Next n lines: student name followed by their scores (space-separated floats)
- Last line: query_name (student to calculate average for)

Output:
- Float (average score of specified student, 2 decimal places)

Example Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Example Output:
56.00

Explanation:
Marks for Malika: [52, 56, 60]
Average = (52 + 56 + 60) / 3 = 56.00

Constraints:
- 2 ≤ n ≤ 10
- 0 ≤ marks ≤ 100
- Each student has between 1-10 scores
"""

if __name__ == '__main__':
    # Read the number of student records
    n = int(input())
    
    # Initialize an empty dictionary to store student data
    student_marks = {}
    
    # Loop through each student record
    for _ in range(n):
        # Split input line into name and scores (using * to capture all remaining values)
        name, *line = input().split()
        
        # Convert scores from strings to floats
        scores = list(map(float, line))
        
        # Store in dictionary: name as key, scores list as value
        student_marks[name] = scores
    
    # Read the name of the student to query
    query_name = input()
    
    # Get the marks list for the queried student
    marks = student_marks[query_name]
    
    # Calculate average: sum of marks divided by count of marks
    average = sum(marks) / len(marks)
    
    # Print formatted to 2 decimal places
    print("{:.2f}".format(average))
    # Alternative using f-string (Python 3.6+):
    # print(f"{average:.2f}")