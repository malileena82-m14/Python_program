'''7.Add Corresponding Elements from Two Sets
Write a Python program to create two sets containing the same number of elements. Convert them into 
lists and calculate the sum of corresponding elements.
Sample Input:
Set 1 = {10, 20, 30}
Set 2 = {1, 2, 3}
Sample Output:
11
22
33'''

'''s1 = {10,20,30}
s2 = {1,2,3}

list1 = list(s1)
list2 = list(s2)

for i in range(3):
    sum = list1[i] + list2[i]
    print(sum)'''
    
s1 = set()
s2 = set()

print("Enter set1 elements : ")
for i in range(3):
    a = int(input())
    s1.add(a)

print("Enter set2 elements : ")   
for i in range(3):
    a1 = int(input())
    s2.add(a1)
    
list1 = list(s1)
list2 = list(s2)

for i in range(len(s1)):
    total = list1[i] + list2[i]
    print(total) 