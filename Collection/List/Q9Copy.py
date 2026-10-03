'''Question 9: Write a java program to copy one array to another array.
Asked In Practice assignment
Input : Array1 = {5, 10, 15, 20}
Output : Array2 = {5, 10, 15, 20}
Explanation:
Copy each element of Array1 into Array2 using index-by-index assignment'''

list1 = [5,10,15,20]

list2 = [0]*len(list1)


for i in range(len(list1)):
    list2[i] = list1[i]
print("Copy Element : ",list2)