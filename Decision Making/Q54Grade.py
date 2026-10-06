'''Question 54: Write a program that takes a grade (A, B, C, D, F) as input and displays the corresponding remark using switch:
? A: Excellent
? B: Good
? C: Average
? D: Poor
? F: Fail
Asked In Just Practice assignment
Input:
Grade = A

Output:
Excellent

Explanation:
The switch matches grade ‘A’ and prints “Excellent”. Each grade has a specific remark.

Input:
Grade = D

Output:
Poor

Explanation:
Grade ‘D’ matches the case and prints “Poor”.'''

ch = input("Enter Input : ")

match ch:
    case 'A' : print("Excellent")
    case 'B' : print("Good")
    case 'C' : print("Average")
    case 'D' : print("Poor")
    case 'F' : print("Fail")
    case _ : print("Invalid")