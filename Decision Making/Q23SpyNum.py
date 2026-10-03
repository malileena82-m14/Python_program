'''Question 23: Write a java program to Check Number Is Spy Number or Not.
Example : A number is said to be a Spy number if the sum of all the digits is equal to the product of all digits.
Asked In Just Practice assignment
Input:
Number = 1412

Output
Spy Number

Explanation:
Sum = 1 + 4 + 1 + 2 = 8
Product = 1 * 4 * 1 * 2 = 8
Since sum = product = 8, it is a Spy Number.'''

n = int(input("Enter number : "))

digit = n//1000
digit1 = (n//100)%10
digit2 = (n//10)%10
digit3 = n%10

s = digit + digit1 + digit2 +digit3 
product = digit * digit1 * digit2 * digit3

if s == product:
    print("Spy Number")

else:
    print("Not Spy Number")

