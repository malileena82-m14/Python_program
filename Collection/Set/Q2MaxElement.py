'''2.Find the Maximum Element
Write a Python program to create a set of integers and find the largest element in the set.'''

'''a = set(input("Enter Elements : ").split())

max = 0
for i in a:
    if int(i) > max:
        max = int(i)
        
print("Maximum Elements : ",max)'''

size = int(input("Enter a size: "))
j = 0
s = set()
while j < size:
    s.add(int(input("Enter a integer element: ")))
    j +=1
max1=0
for i in s:
    if max1<i:
        max1=i
print("Maximum Element",max1)
'''s = list(s)
for i in range(len(s)-1):
    if s[i] > s[i+1]:
        s[i+1] = s[i]
print("max value is : ",s[-1])'''

        



