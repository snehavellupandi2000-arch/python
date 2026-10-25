#Sum and Average of All Numbers in a List

numbers = [71, 12, 3, 4, 5.9]
total = sum(numbers)
average = total / len(numbers)
print("sum of list =", total)
print("Average of list =", average)

#max and min
print(max(numbers))
print(min(numbers))

# product of all numbers
mul = 1
for i in numbers:
    mul = i*mul
print("value of product of list is ", mul)

#even odd
even = 0
odd = 0
for i in numbers:
    if i%2 == 0:
        even+=1
    else:
        odd+=1
print (even)
print(odd)

#copy list
b=numbers
print(b)

#sort and descend list
numbers.sort()   #ascending order
print(numbers)

numbers.reverse() #descending order
print(numbers)

# combine list1 and list2
list1 = ["abe", 6]
list2 = ["def", 45]

print(list1+list2)
