'''Q.5 Dictionary Update
Write a Python program to create a dictionary containing three key-value pairs. 
Ask the user for a key and a new value, then update the dictionary with the new value. 
Display the updated dictionary.'''

dictionary = {}

for i in range(3):
    Id = int(input("Enter Student Id : "))
    name = input("Enter Student Name : ")
    dictionary[Id] = name
    
update_id = int(input("Enter Update Id : "))
update_name = input("Enter Update name : ")
dictionary[update_id] = update_name

for k,v in dictionary.items():
    print(k,"\t",v)