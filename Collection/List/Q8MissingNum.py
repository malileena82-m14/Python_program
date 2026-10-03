'''Question 8: Write a java program to find missing elements in an array.
Asked In Practice assignment
Input : Array = {1, 2, 4, 5, 7} (numbers from 1 to 7 should be present)
Output : Missing elements = {3, 6}
Explanation:
Check sequence numbers one by one.If a number from 1 to maximum (7) is not in the array, it is missing.'''


list = [1,2,4,5,7]
max =7

print("Missing Number : ",end="")
for i in range(1,max+1):
    flag = 0 
    for j in range(len(list)):
        if list[j] == i:
            flag =1
            break
        
    if flag==0:
        print(i,end=" ")
        
