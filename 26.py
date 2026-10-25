#function
# def - defining function
# syntax - 
"""def m(a,b):
    print("Sneha")
    print(a+b)
m(2,3)"""
#  sum, diff. mul and division
"""def calculation(a,b):
    print("sum :", a+b)
    print("sub :", a-b)
    print("product :", a*b)
    print("div :", a/b)
calculation(4,5)

#ex1 max number
def max(n1,n2, n3):
    if n1>n2 and n1>n3 :
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3
print("maximum number is" ,max(2,3,1))

#sum of all numbers in list
list1 = [1, 2, 3, 4, 5]
def addList(list1):
    total = 0
    for i in list1:
        total = total + i
    return total

print("addition of list", addList(list1))

#multiplication of all numbers in list

def mulList(list1):
    mul = 1
    for i in list1:
        mul = mul*i
    return mul

print("multiplication of list", mulList(list1))"""

"""#even number in list
list1 = [1, 2, 3, 4, 5]
def even(list1):
    for i in list1:
        if i % 2 == 0:
            print(i,  end=" ")
even(list1)"""

#factorial
def factorial(a):
    num = 1
    for i in range(1, a+1):
        num = num*i
    return num
print("factorial of given number: ", factorial(5))
