'''Question 10: Write a java program to count the number of digits in a number
Asked In Just Practice assignment
Input:

Number = 12345

Output:

Number of digits = 5

Explanation:

The program divides the number by 10 repeatedly until it becomes 0.
Each division reduces one digit, and a counter keeps track of total digits.'''

n = int(input("Enter number : "))
count=0
while n>0:
    d = n%10
    count +=1
    n = n//10
    
print("Number of Digits : ",count)