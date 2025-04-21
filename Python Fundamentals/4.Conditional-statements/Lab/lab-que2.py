""" Write a Python program to check if a number is prime using if_else. """

num = int(input("Enter any number :"))

if num <= 1:
    print(num, "is not a prime number.")
elif num == 2:
    print("2 is a prime number.")
else:
    is_prime = True  
    for i in range(2, int(num/2)+1):  
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")