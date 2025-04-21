""" Write a Python program to find greater and less than a number using 
if_else. """

num1 = int(input("Enter number 1 : "))

num2 = int(input("Enter number 2 : "))

if num1>num2:
    print(f"{num1} - number 1 is greater and {num2} - number 2 is smaller")
else:
    print(f"{num1} - number 1 is smaller and {num2} - number 2 is greater")