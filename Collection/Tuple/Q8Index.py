'''Q8 Find the index of a given element in a tuple.'''

a = (10,20,30,40,50,80,60)
num = int(input("Enter number : "))
for i in range(len(a)):
    if a[i]==num:
        break;
print("index of Given Element : ",i)