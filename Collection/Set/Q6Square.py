'''6.Find the Square of Each Element
Write a Python program to create a set of integers and create a new set containing the square of each
element.'''

'''a = {1,2,3,4,5}
s =set()

for i in a:
    s.add(i*i)
    
print("Square of each Element : ",s)'''

n = int(input("Enter size : "))
s = set()

print("Enter Element : ")
for i in range(n):
    a = int(input())
    s.add(a)

s1 = set()    
for i in s:
    s1.add(i*i)
    
print("Square of each Element : ",s1)