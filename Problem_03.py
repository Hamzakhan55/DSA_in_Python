# Right-Aligned Right-Angled Triangle

num = int(input("Enter a number: "))

for i in range(1, num+1):
    spaces = num - i
    stars = i
    print(" " * spaces +  "*" * stars)
    
    
    
# Output

# Enter a number: 5
#     *
#    **
#   ***
#  ****
# *****