'''Q1. Division of Two Numbers
Write a Python program to divide two numbers. Handle the exception that occurs when the denominator is zero.'''

a = int(input("Enter num1 : "))
b = int(input("Enter num2 : "))
try:
    c = a//b
    print(c)
except ZeroDivisionError as t:
    print("Division not successfully")