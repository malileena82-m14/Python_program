'''Question 6: Write a java program to find the sum of all natural numbers between 1 to n.
Asked In Just Practice assignment
Input:

n = 5

Output:

Sum = 15

Explanation:

The program adds numbers from 1 to 5.
1 + 2 + 3 + 4 + 5 = 15.'''

'''n = int(input("Enter number : "))

i=1
sum =0
while i<=n:
    sum = sum+i
    i+=1
print("Sum : ",sum)'''

n = int(input("Enter number : "))
sum = 0
for i in range(1,n+1,1):
    sum = sum+i
print("Sum : ",sum)