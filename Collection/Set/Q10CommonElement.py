'''10.Find Common Even Numbers
Write a Python program to create two sets and display the common elements that are even numbers.
Sample Input:
Set 1 = {2, 3, 4, 5, 12, 35}
Set 2 = {1,2,5,4,6,12}
Sample Output:
2
4
12'''

s1 = set()
s2 = set()

n = int(input("Enter Size : "))
print("Enter Set1 : ")
for i in range(n):
    a = int(input())
    s1.add(a)
    
n1 = int(input("Enter Size : "))
print("Enter Set2 : ")
for i in range(n1):
    a1 = int(input())
    s2.add(a1)
    
print("Common Elements : ")
for i in s1:
    for j in s2:
        if i%2==0 and i==j:
            print(i)
            
