'''Q.2 Employee Salary Record
Write a Python program to take an employee ID and salary as input and store them in a dictionary. 
Display the employee ID and salary.'''

Employee = {}
for i in range(3):
    Id = int(input("Enter Employee Id : "))
    sal = int(input("Enter Employee Salary : "))
    Employee[Id] = sal
    
print("\nDisplay Employee id and Salary ")
for k,v in Employee.items():
    print(k,"\t",v)
    