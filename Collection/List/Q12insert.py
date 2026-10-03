'''Question 12: Write a program in java to insert an element at desired position from an array.
Asked In Practice assignment
Input the size of array : 6

Input 5 elements in the array in ascending order :
1 2 3 4 5

Input the position where to insert : 2
Value : 200

Expected Output : The new list is : 1 2 200 3 4 5'''

n = int(input("Enter Size : "))

list = [0]*n

print("Enter Elements : ")
for i in range(n-1):
    list[i] = int(input(""))
    
pos = int(input("Position insert in index : "))
value = int(input("Enter number : "))
for i in range(n-1,pos-1,-1):
    list[i] = list[i-1]
    
list[pos]= value   
print("New List : ",list,end="")