'''19 Create a tuple of numbers and calculate their sum.'''

n = int(input("Enter Size : "))
a = ()

for i in range(n):
    x = int(input("Enter Values : "))
    a = a + (x,)
    
sum =0
for i in range(len(a)):
    sum = sum+a[i]
print(sum)