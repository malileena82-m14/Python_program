'''Q9 Check if an element exists in a tuple.'''

a = (10,20,50,90)
num = int(input("Enter Values : "))
for i in range(len(a)):
    if a[i]==num:
        print("Element are Present")
        break
else:
    print("Element are not Present")
        