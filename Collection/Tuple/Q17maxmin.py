'''Q17 Find the maximum and minimum value in a tuple.'''

n = int(input("Enter Size : "))
a = ()

for i in range(n):
    x = int(input("Enter Values : "))
    a = a + (x,)
    
max = a[0]
min = a[0]
 
for i in range(len(a)):
    if max<a[i]:
        max = a[i]
        
    elif min>a[i]:
        min = a[i]
        
print("Max : ",max)
print("Min : ",min)