'''Q7 Count how many times a specific value appears in a tuple.'''

a = (10,20,20,50,80,50)
count =0
num = int(input("Enter Number : "))
for i in a:
    if a[i]==num:
        count = count+1
print(count)

'''n = int(input("Enter Size"))
a = ()

for i in range(n):
    x = int(input("Enter Values : "))
    a = a + (x,)
    
num = int(input("Enter number : "))

count =0
for i in range(n):
    if a[i]==num:
        count = count+1
        
print(count)'''