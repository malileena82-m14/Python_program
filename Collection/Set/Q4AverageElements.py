'''4. Calculate the Average of Set Elements
Write a Python program to create a set of integers and calculate the average of all elements.'''

a = {1,2,3,4,5}
sum =0
for i in a:
    sum = sum +i
avg = sum//len(a)
print("Average : ",avg)