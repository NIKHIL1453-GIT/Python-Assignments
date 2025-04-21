age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))


if age >= 18:
    if weight >= 55:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood because your weight is less than 55 kg.")
else:
    print("You are not eligible to donate blood because your age is less than 18.")