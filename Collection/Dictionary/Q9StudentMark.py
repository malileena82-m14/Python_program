'''Q.9 Subject Marks
Write a Python program to take subject names and marks for three subjects and store them in a dictionary
Display all subjects and marks and calculate the average marks.'''

subject = {}
for i in range(3):
    name = input("Enter Student Name : ")
    mark = int(input("Enter Student Mark : "))
    subject[name] = mark

print("Average marks : ") 
sum = 0
for k,v in subject.items():
    sum =sum+
avg = sum/3
print(avg)    
    