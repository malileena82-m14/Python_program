'''Q11 Repeat a tuple 3 times.'''

n = int(input("Enter Size : "))
a = ()

for i in range(n):
    x = int(input("Enter Values : "))
    a = a + (x,)
print("Repeat Tuple : ",a*3)