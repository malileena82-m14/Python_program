'''Q3 Access the third element of a tuple.'''

'''a = (10,20,30,"Leena",40)
print(a[2])'''

n = int(input("Enter Size : "))
a = ()

for i in range(n):
    x = input("Enter Values : ")
    a = a +(x,)
    
l1 = list(a)
print(l1)
print("Third Element : ",a[2])
