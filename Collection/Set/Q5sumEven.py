'''5.Find the Sum of Even Numbers
Write a Python program to create a set of integers and calculate the sum of only the even numbers.'''

'''a = {1,2,3,4,5,6}

sum =0
for i in a:
	if i%2==0:
		sum = sum+i
print("Sum of Even Number : ",sum)'''

n = int(input("Enter Size : "))
s = set()

print("Enter Elements : ")
for i in range(n):
    a = int(input())
    s.add(a)

esum =0
for i in s:
    if i%2==0:
        esum = esum+i
print("Sum of Even Numbers : ",esum)
