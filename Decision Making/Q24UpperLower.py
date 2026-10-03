'''Question 24: Write a java program to check whether a character is uppercase or lowercase alphabet.
Asked In Just Practice assignment
Input:
Character = A

Output
Uppercase Alphabet

Explanation:
Character 'A' lies between 'A' and 'Z', so it is uppercase.'''

ch = input("Enter Character : ")

if ch>='A' and ch<='Z' :
    print("UpperCase Alphabet")
    
elif ch>='a' and ch<='z':
    print("Lower Alphabet")
    
else:
    print("Not UpperCase and LowerCase")