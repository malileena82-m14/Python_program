'''Question 7: Write a java program to display the reverse array.
Asked In Practice assignment
Input : Array = {1, 2, 3, 4, 5}
Output : Reverse array = {5, 4, 3, 2, 1}
Explanation :
The last element becomes the first, and the first becomes the last by traversing from the end to the start.'''

list = [1,2,3,4,5]
print("Before list : ",list)

l=0
r= (len(list)-1)

while l<r:
    temp = list[l]
    list[l] = list[r]
    list[r] = temp
    
    l = l+1
    r = r-1
    
print("After reverse : ",list)
