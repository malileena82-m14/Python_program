'''Question 6: Write a java program to search an element in an array , its element found or not.
Asked In Practice assignment
Input:
Array = {10, 20, 30, 40, 50}
Element to search = 30
Output : Element 30 found at index 2
Explanation :
We traverse the array and compare each element with the search key. If it matches, print "found" with index; 
otherwise print "not found".'''

list = (input("Enter Element : ")).split()

skey = (input("Element Search Key : "))

for i in range(len(list)):
    if list[i]==skey:
        flag = bool(True)
        break
        
if flag==True:
    print("Element ",skey," found at index ",i) 
