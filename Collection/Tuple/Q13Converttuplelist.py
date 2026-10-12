'''Q13 Convert a tuple into a list.'''

n = int(input("Enter Size : "))
a = ()

for i in range(n):
    x = (input("Enter Values : "))
    a = a + (x,)
    
l1 = list(a)
print(l1)