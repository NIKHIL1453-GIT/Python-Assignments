"""Write a Python program that manipulates and prints strings using various string methods."""

str1 = "nikhil"

str2 = "BHATIA"

str3 = "nikhil bhatia"

print(f"Upper case:{str1.upper()}")
print(f"Lower case:{str2.lower()}")
print(f"capitalize Methods:{str1.capitalize()}")
print(f"title Method:{str3.title()}")
print(f"find Method:{str3.find("bhatia")}")

if str1.endswith("il"):
    print(f"{str1} - This string end with il")

if str2.startswith("BH"):
    print(f"{str2} - This string starts with BH")