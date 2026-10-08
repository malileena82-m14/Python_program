'''9.Find the Product of All Elements
Write a Python program to create a set of integers and calculate the product of all elements.'''

n = int(input("Enter Size : "))
s = set()

print("Enter Elements : ")
for i in range(n):
    a = int(input())
    s.add(a)
    
print("Product of all Elements : ")
prod = 1
for i in s:
    prod = prod*i
print(prod)