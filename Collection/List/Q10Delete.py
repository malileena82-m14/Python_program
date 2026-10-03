'''Question 10: Write a program in java to delete an element at desired position from an array.
Asked In Practice assignment
Input the size of array : 5

Input 5 elements in the array in ascending order :  1 2 3 4 5

Input the position where to delete : 3

Expected Output : The new list is : 1 2 4 5'''

n = int(input("Enter Size : "))

list = [0]*n

print("Enter Elements : ")
for i in range(n):
    list[i] = int(input())
    
pos = int(input("Position to delete : "))

for i in range(pos-1,n-1):
    list[i] = list[i+1]
n=n-1

print("New List is : ",end="")

for i in range(n):
    print(list[i],end=" ")