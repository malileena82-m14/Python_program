'''Q16 Iterate through a tuple using a while loop.'''

n = int(input("Enter Size : "))
a = ()

for i in range(n):
    x = int(input("Enter Values : "))
    a = a + (x,)
    
i=0
while i<n:
    print(a[i])
    i=i+1