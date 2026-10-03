'''Question 11: Write a java program to give an array, find the second largest element.
Asked In Practice assignment
Input : Array = {12, 35, 1, 10, 34, 1}
Output : Second largest = 34
Explanation:
First largest is 35, second largest is the next maximum (34). We maintain two variables (largest, secondLargest).'''

list = [12,35,1,10,34,1]


max = list[0]
sm = list[0]
for i in range(len(list)):
    if list[i]>max:
        sm = max
        max = list[i]
        
    elif list[i]<max and list[i]>sm:
        sm = list[i]
        
print("Second Largest Number : ",sm)