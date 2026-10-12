'''Q2. Integer Input
Write a Python program to accept an integer from the user. Handle the exception if the user enters a non-numeric value.'''


try: 
    n = int(input("Enter input : "))
    print(n)
except ValueError as t:
    print("It is non-numeric value")
