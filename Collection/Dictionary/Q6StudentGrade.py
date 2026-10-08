'''Q.6 Student Grade Dictionary
Write a Python program to take a student's name and percentage as input. Store the student's name and 
grade in a dictionary based on the following criteria:
75 and above → A
60 to 74     → B
40 to 59     → C
Below 40     → Fail'''

student = {}

for i in range(3):
    name = input("Enter Student Name : ")
    per = int(input("Enter percentage : "))
    student[name] = per
    
    if per>=75:
        student[name] = 'A'
        
    elif per<=74 and per>=60:
        student[name] = 'B'
        
    elif per<=59 and per>=40:
        student[name] = 'c'
        
    elif per>40:
        student[name] = "Fail"
        
print("Display Student Record : ")
for k,v in student.items():
    print(k,"\t",v)