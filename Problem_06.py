# Write a Python program that asks the user to enter an integer n.
# Your program should print an inverted centered pyramid pattern made of * symbols with n rows.

num = int(input("Enter number of rows for inverted pyramid: "))

for i in range(num, 0, -1):
    spaces = num - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars + " " * spaces)
    
    
# OutPut

# Enter number of rows for inverted pyramid: 5
# *********
#  ******* 
#   *****  
#    ***   
#     *   