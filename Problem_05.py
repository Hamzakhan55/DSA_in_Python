# Centered Pyramid

num = int(input("Enter number of rows for Pyramid: "))

for i in range(1, num+1):
    spaces = num - i
    stars = 2 * i -1
    print(" " * spaces + "*" * stars + " " * spaces)
    
    
    
# OutPut

# Enter number of rows: 5
#     *    
#    ***
#   *****
#  *******
# *********