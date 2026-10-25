# Basic operations
dictA = {
    "Name": "Sneha",
    "Age": 30
}

print(dictA) #{'Name': 'Sneha', 'Age': 30}
print(dictA["Name"]) # Sneha will be printed
dictA["Age"] = 25 
print(dictA) #{'Name': 'Sneha', 'Age': 25}
dictA["Gender"] = "Female"
print(dictA) #{'Name': 'Sneha', 'Age': 25, 'Gender': 'Female'}

#Exercise 2: Dictionary Operations
# Add new key
dictA["course"] = "Python"
print(dictA) #{'Name': 'Sneha', 'Age': 25, 'Gender': 'Female', 'course': 'Python'}
# Update value
dictA["Age"] = 26
print(dictA) #{'Name': 'Sneha', 'Age': 26, 'Gender': 'Female', 'course': 'Python'}
# Delete key
del dictA["Gender"]
print(dictA) #{'Name': 'Sneha', 'Age': 26, 'course': 'Python'}

# Exercise 3: Dictionary from Two Lists
list1 = ["name", "age", "city"]
list2 = ["Sneha", 25, "Chennai"]

student = dict(zip(list1, list2))

print(student)

#Exercise 4: Clear Dictionary

person = {"name" : " Sneha", "age" : 25}
person.clear()
print(person)

#Exercise 5: Merge Dictionaries
student1 = {"name" : " Sneha", "age" : 25}
student2 = {"city" : " Chennai", "gender" : "FEMALE"}
merged_dict = {**student1, **student2}
print(merged_dict)

#Exercise 6: Access Nested Dictionary
person1 = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}, "age":30}
print(person1["name"])
print(person1["age"])
print(person1["address"]["zip"])
print(person1["address"]["city"])


#Exercise 7: Access ‘history’ Key From a Nested Dictionary
person2 = {"name": "Carol", "address": {"city": "Paris", "zip": "75001", "history": 95}, "age":30, }
print(person2["address"]["history"])

#Exercise 8: Initialize Dictionary with Default Values
keys = ["math", "science", "english", "history"] 
default = 0
default_dict = dict.fromkeys(keys,default)
print(default_dict)

#Exercise 9: Rename a Key of Dictionary
student3 = {"name" : " Sneha", "age" : 25}
student3["student_name"] = student3.pop("name")
print(student3)

#Exercise 10: Delete a List of Keys
student4 = {"name" : " Sneha", "age" : 25}
keys = ["name"]
for i in keys:
    student4.pop(i)
print(student4)
