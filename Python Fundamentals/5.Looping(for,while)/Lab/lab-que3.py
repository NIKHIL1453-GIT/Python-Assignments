""" Write a Python program to find a specific string in the list using a simple 
for loop and if condition. """


List1 = ['apple', 'banana', 'mango']

fruit = input("Enter fruit name : ")

for i in List1:
    if i == fruit:
        print(f"{i} found!!!")
    else:
        print(f"{fruit} - Not found")
        