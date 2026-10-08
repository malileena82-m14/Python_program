'''Q.7 Display the dictionary. Country and Capital
Write a Python program to take the names of three countries and their capitals from the user and store them in a dictionary.
Display all country-capital pairs.'''

countries = {}

for i in range(3):
    country = input("Enter Country names : ")
    capital = input("Enter Capitals names : ")
    countries[country] = capital
    
for k,v in countries.items():
    print(k," ",v)