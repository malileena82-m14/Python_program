'''Q15 Iterate through a tuple using a for loop.'''

n = int(input("Enter Size : "))
a = ()

for i in range(n):
    x = int(input("Enter Values : "))
    a = a + (x,)
    
for i in range(len(a)):
    print(a[i])