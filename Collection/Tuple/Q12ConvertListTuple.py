'''Q12 Convert a list into a tuple.'''

n = int(input("Enter Size : "))
list = [0]*n

for i in range(n):
    list[i]= (input("Enter Values : "))
    
a = tuple(list)
print(a)