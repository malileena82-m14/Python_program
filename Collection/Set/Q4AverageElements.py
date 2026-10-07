'''4. Calculate the Average of Set Elements
Write a Python program to create a set of integers and calculate the average of all elements.'''

'''a = {1,2,3,4,5}
sum =0
for i in a:
    sum = sum +i
avg = sum//len(a)
print("Average : ",avg)'''

n = int(input("Enter size : "))
s = set()

print("Enter elements : ")
for i in range(n):
    a = int(input())
    s.add(a)
    
sum=0
for i in s:
    sum = sum+i
avg = sum//n
print("Average : ",avg)
