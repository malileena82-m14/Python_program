'''Question 9: Write a java program to print a multiplication table of any number.
Asked In Just Practice assignment
Input:

Number = 5

Output:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

Explanation:

The program multiplies the given number by values from 1 to 10.
Each result is printed in table format.'''

n = int(input("Enter number : "))

'''i=1
while i<=10:
    m=i*n
    i+=1
    print(m)'''
    
for i in range(1,10+1,1):
    print(n*i)