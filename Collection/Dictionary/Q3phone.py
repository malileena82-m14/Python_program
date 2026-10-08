'''Q.3 Phone Book
Write a Python program to take a person's name and phone number as input and store them in a dictionary.
Ask the user for a name and display the corresponding phone number.'''

phone = {}

for i in range(2):
    name = input("Enter name : ")
    number = int(input("Enter phone number : "))
    phone[name] = number
sname = input("Search : ")
print("Display Person Record : ")
for k,v in phone.items():
    if sname == k:
        print(k,"\t",v)