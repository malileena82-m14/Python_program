'''Q20 Unpack a tuple into different variables.'''

n = int(input("Enter Size : "))
a =()

for i in range(n):
    x = int(input("Enter Values : "))
    a = a + (x,)
    
b,c,d,*e = a

print(b,"\t",c,"\t",d,"\t",e)