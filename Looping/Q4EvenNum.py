'''Question 4: Write a java program to print all even numbers between 1 to 100.using while loop
Asked In Just Practice assignment
Input:

No input required

Output:

2 4 6 8 ... 100

Explanation:

Even numbers are divisible by 2.
The program checks each number from 1 to 100 and prints it if it is divisible by 2.'''

'''i = 1

while i<=100:
    if i%2==0:
        print(i,end=" ")
    i+=1'''

for i in range(1,100,1):
    if i%2==0:
        print(i,end=" ")