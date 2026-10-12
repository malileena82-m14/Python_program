'''Q1.Create a tuple with 5 integer values and print it.'''

'''a =(10,20,30,40,50)
print(a)'''

n = int(input("Enter size : "))
a = ()

for i in range(n):
    x = int(input("Enter Values : "))
    a = a + (x,)
    
print(a)