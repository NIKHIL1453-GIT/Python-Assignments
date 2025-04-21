""" Print this pattern using nested for loop: 
  
* 
** 
*** 
**** 
*****

"""
row = int(input("Enter Row Count:")) 
 
for i in range (1,row):
    for j in range(0,i):
        print("* ",end=" ")
    print()