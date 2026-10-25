set1 = {1,2,3}
set2 = {3,4,5,6}
set3 = {12,32,12,32,14}
empty_set ={}

# Exer - 1 Basic set operations
set1.add(6)
print(set1)
set1.remove(6)
print(set1)

#Exer-2 Clear all elements
set3.clear()
print(set3)

#Exer-3  Find the Length of a Set
print(len(set2)) # print 4

#Exer-4 Set empty
if  empty_set == {}:
    print("set1 is empty")
else:
    print("set is not empty it has elements")

#Exer-5 union: combine

union_set = set1 | set2
print(union_set) # output {1,2,3,4,5,6}

##Exer-6 intersection: comman elements
intersection_set = set1&set2
print(intersection_set) # output{3}

# Exer-7 difference: finds elements in the set that are not in second
difference_set = set1-set2
print(difference_set) # output{1,2}

# Exer-9 Max and min
set4 ={2,4,12,567,0}
print(max(set4)) # 567
print(min(set4)) # 0


# sum of set elements
#set1 = {1,2,3}
sum = sum(set1)
print(sum) # print 6
