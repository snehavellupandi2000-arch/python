"""a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))

if a > b and a > c:
    print("Greatest number is", a)
elif b > a and b > c:
    print("Greatest number is", b)
else:
    print("Greatest number is", c)"""

"""b = 8
if(b%3 == 0 or b%4 ==0):
    print("b is divisible by 3 or 4")
else:
    print("b is not divisible by 3 or 4")"""

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 76 and marks <= 100:
    print("Grade A")
elif marks >= 51 and marks <= 75:
    print("Grade B")
elif marks >= 26 and marks <= 50:
    print("Grade C")
else:
    print("Grade D")





