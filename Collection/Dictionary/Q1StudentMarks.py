'''Q.1 Student Marks Dictionary
Write a Python program to take a student name and marks as input and store them in a dictionary. 
Display the student name and marks.'''

Student = {}

for i in range(3):
    name = input("Enter Name : ")
    marks = input("Enter Marks : ")
    Student[name] = marks

print("Display Student Data")
for k,v in Student.items():
    print(k,"\t",v)