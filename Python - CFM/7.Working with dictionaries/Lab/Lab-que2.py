# Write a Python program to merge two lists into one dictionary using a loop.


key_list = ["name","CGPA","Center_Code"]
val_list = ["nikhil",7.5,26]

dict = {}

for i in range(len(key_list)):
    dict[key_list[i]] = val_list[i]

print(dict)