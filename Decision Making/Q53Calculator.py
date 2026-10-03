'''Question 53: Create a Java program to simulate a simple calculator using a switch case. It should take two numbers 
and an operator (+, -, *, /, %) as input and perform the corresponding operation.
Asked In Just Practice assignment
Input:
Number1 = 10
Number2 = 5
Operator = +

Output:
Result = 15

Explanation:
The program uses switch on the operator. When '+' is selected, it performs addition of the two numbers.

Input:
Number1 = 10
Number2 = 4
Operator = %

Output:
Result = 2

Explanation:
The '%' operator calculates the remainder after division. 10 % 4 gives remainder 2.'''

print("Choose Operator")
print("+,-,*,/,%")

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
ch = input("Choose Operator : ")


match ch:
    case '+' : print("Addition : ",num1+num2)
    case '-' : print("Subtraction : ",num1-num2)
    case '*' : print("Multiplcation : ",num1*num2)
    case '//' : print("Division : ",num1//num2)
    case '%' : print("modules : ",num1%num2)
    case _ : print("Invalid Operator")
    


