'''Q4 Print the last element of a tuple using negative indexing.'''

'''a = (10,20,30,40,50)
print(a[-1])'''

n = int(input("Enter Size : "))
a = ()

for i in range(n):
    x = int(input("Enter Values : "))
    a = a + (x,)
    
print("Negative indexing : ",a[-1])