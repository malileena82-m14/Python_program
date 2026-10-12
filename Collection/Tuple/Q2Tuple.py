'''Q2 Create a tuple with different data types (int, float, string, bool).'''

'''a = (10,2.5,"Leena",True)
print(a)'''

a =()

i = int(input("Enter Integer : "))
a = a +(i,)

f = float(input("Enter Float : "))
a = a + (f,)

s = input("Enter String : ")
a = a + (s,)

b = bool(True)
a = a + (b,)

print(a)