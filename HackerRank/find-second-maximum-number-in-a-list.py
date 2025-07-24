if __name__ == '__main__':
    n = int(input()) #Reads the number of elements (5)
    arr = list(map(int, input().split())) # Reads the numbers: [2, 3, 6, 6, 5]
    unique_scores = sorted(set(arr), reverse=True)# Removes duplicates and sorts in descending order: [6, 5, 3, 2]
    print (unique_scores[1]) # Prints the second highest score (5)