'''8.Find the Difference Between Maximum and Minimum
Write a Python program to create a set of integers and calculate the difference between the maximum and
minimum elements.'''

n = int(input("Enter Size : "))
s = set()

print("Enter Elements : ")
for i in range(n):
    a = int(input())
    s.add(a)
    
'''maximum = max(s)
minimum = min(s)

diff = maximum - minimum'''
mx = 0
mn = max(s)
for i in s:
    if mx<i:
        mx = i
    if i<mn:
        mn = i
diff = mx - mn
print("Maximum : ",mx)
print("Minimum : ",mn)
print("Difference : ",diff)
    