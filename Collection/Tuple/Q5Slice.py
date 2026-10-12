'''Q5 Slice a tuple to print elements from index 1 to 4.'''

'''a = (10,20,30,40,50)
print(a[1:4])'''

n = int(input("Enter Size : "))
a = ()

for i in range(n):
    x = int(input("Enter Values : "))
    a = a + (x,)
    
s = int(input("Start Index : "))
e = int(input("End Index : "))

print(a[s:e])