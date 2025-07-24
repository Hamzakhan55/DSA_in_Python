# Right-Aligned Inverted Right-Angled Triangle

num =  int(input("Enter the number: "))

for i in range(num, 0, -1):
    spaces = num - i
    stars = i
    print(" " * spaces + "*" * stars)
    
    
# Output

# Enter the number: 5
# *****
#  ****
#   ***
#    **
#     *