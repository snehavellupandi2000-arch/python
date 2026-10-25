# Basic Tuple Operations
tuple1 = (12, 56.7, "Tuple", True)
tuple2 = ("a", False)
stringA = ("a")
stringB = "b"

tuple3 = ("a",)

print(tuple1)
print(tuple1[1])  # print 56.7
print(tuple1[3])  # print True

# Tuple Repetition
print(tuple1*3) #(12, 56.7, 'Tuple', True, 12, 56.7, 'Tuple', True, 12, 56.7, 'Tuple', True)

 # The Trailing Comma
print(type(stringA)) # print <class 'str'>
print(type(stringB)) # print <class 'str'>
print(type(tuple3)) # print <class 'tuple'>
print(type(tuple1)) # print <class 'tuple'>

#Tuple Slicing
print(tuple1[1:2]) #output -- 56.7

# Tuple concartination
print(tuple1+tuple2) # (12, 56.7, 'Tuple', True, 'a', False)

#Tuple Reversal
print(tuple1[::-1]) # (True, 'Tuple', 56.7, 12)


# tuple counting
tuple4 = (12, 2, 2, 2, 56.7, "Tuple", True, False)
print(len(tuple4)) # print 8

# unpacking
details = ("Sneha", 25, "Female")
name, age, gender = details
print(name) # Sneha
print(age) # 25
print(gender) # Female

#The Swap Trick
tupleA = (12, 56.7, "Tuple", True)
tupleB = ("a", False)
tupleA, tupleB = tupleB, tupleA
print(tupleA) # ("a", False)
print(tupleB) #  (12, 56.7, "Tuple", True)

#Nested Tuple Access
tupleX = (12, 56.7, (True, 1), "Tuple", True, ("Python", 3,14))
#          0    1       2           3     4         5
#                      0    1                       0       1
#                               01234           012345
print(tupleX[2][0])  # True
print(tupleX[3][3]) # l
print(tupleX[5][0][4]) # o