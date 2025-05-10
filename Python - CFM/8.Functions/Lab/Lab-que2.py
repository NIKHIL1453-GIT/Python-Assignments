# Write a Python program to create a calculator using functions. 
def addition():
    print(f"addition of {num1} and {num2}  = {num1 + num2}")

def subtraction():
    print(f"subtraction of {num1} and {num2}  = {num1 - num2}")

def multiplication():
    print(f"multi of {num1} and {num2}  = {num1 * num2}")

def division():
    print(f"divi of {num1} and {num2} = {num1 / num2}")

menu = """ 
                Menu 

                    press 1 for addition 
                    press 2 for subtraction
                    press 3 for multi 
                    press 4 for div 
"""
print(menu)

choice = int(input("Enter your choice:"))

if choice == 1:
    print("Enter 2 numbers:")
    num1 = int(input("Enter number 1 :"))
    num2 = int(input("Enter number 2 :"))

    addition()
elif choice == 2:
    print("Enter 2 numbers:")
    num1 = int(input("Enter number 1 :"))
    num2 = int(input("Enter number 2 :"))

    subtraction()
elif choice == 3:
    print("Enter 2 numbers:")
    num1 = int(input("Enter number 1 :"))
    num2 = int(input("Enter number 2 :"))

    multiplication()
elif choice == 4:
    print("Enter 2 numbers:")
    num1 = int(input("Enter number 1 :"))
    num2 = int(input("Enter number 2 :"))

    division()
else:
    print("Invalid choice")