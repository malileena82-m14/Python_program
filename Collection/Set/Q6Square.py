'''6.Find the Square of Each Element
Write a Python program to create a set of integers and create a new set containing the square of each
element.'''

a = {1,2,3,4,5}
s =set()

for i in a:
    s.add(i*i)
    
print("Square of each Element : ",s)
