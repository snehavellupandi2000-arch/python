'''Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.'''
"""number1 = int(input("enter first number "))
number2 = int(input("enter second number "))
product = number1*number2
if product<=1000:
    print("Product of two numbers :", product)
else:
    print("sum of two numbers :", number1+number2)
"""
''' Display only those characters which are present at an even index number in given string.'''
'''str = input("enter the string :")
for i in range(0, len(str), 2):
    print(str[i])
'''
'''
prev_num = 0

# Loop from 0 to 9
for i in range(10):
    x = prev_num + i
    print(f"Current Number {i} Previous Number {prev_num} Sum: {x}")
    
    # Update previous_num for the next iteration
    prev_num = i
'''

#Write a function to remove characters from a string starting from index 0 up to n and return a new string.
'''given_string = "My name is Sneha"

def removeCharacters(n):
    new_string = given_string[n:]
    return new_string

print(removeCharacters(4))
print(removeCharacters(2))
'''
'''for i in range(10,55,2):
    print("The even occourence is:", i)
for j in range(11,55,2):
    print("The odd occurance is:", j)'''
# User input for number of rows
rows = int(input("Enter the rows:")) 
# Outer loop will print number of rows 
for i in range(0,rows+1): 
# Inner loop will print number of Astrisk 
    for j in range(i): 
        print("1*2",end = '') 
    print() 