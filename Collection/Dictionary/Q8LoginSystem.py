'''Q.8 Simple Login System
Write a Python program to create a dictionary containing usernames and passwords. 
Ask the user to enter a username and password and check whether the login details are correct.'''

login = {}

for i in range(2):
    u = input("Enter User Names : ")
    p = int(input("Enter Password : "))
    login[u] = p
    
username = input("check user name : ")
password = int(input("check password : "))

for k,v in login.items():
    if username == k and password == v:
        print(k,"\t",v)
        print("Login details Are correct")
        break
else:
    print("Login details Are not correct")    
        