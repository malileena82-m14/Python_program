'''Q10 Concatenate two tuples.'''

'''a = (10,20,30,40,50)
b = (60,70,80,90,100)

t = a + b

print(t)'''

n = int(input("Enter Size : "))
a = ()
b = ()

for i in range(n):
    x = int(input("Enter Values A : "))
    a = a + (x,)
    
for i in range(n):
    x = int(input("Enter Values B : "))
    b = b + (x,)
    
print("Concatenate two tuple : ",a + b)