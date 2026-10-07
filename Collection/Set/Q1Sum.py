'''1. Find the Sum of All Elements in a Set
Write a Python program to create a set of integers and calculate the sum of all elements.'''

'''n = set(input("Enter Elements : ").split())
sum = 0
for i in n:
    sum = sum + int(i)
print("Sum of all elements : ",sum)'''

a = set()
a.add(10)
a.add(20)
a.add(30)
a.add(40)
a.add(50)

sum = 0
for i in a:
    sum = sum + int(i)
print("Sum of all Elements : ",sum)