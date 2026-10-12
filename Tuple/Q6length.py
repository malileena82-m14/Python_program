'''Q6 Find the length of a tuple.'''

'''a =(10,20,30,80,50,80)
count = 0
for i in a:
    count = count + 1
print("Length : ",count)'''

n = int(input("Enter Size : "))
a =()
count =0
for i in range(n):
    x = int(input("Enter Values : "))
    a = a + (x,)
    count =count+1
    
print("Length : ",count)