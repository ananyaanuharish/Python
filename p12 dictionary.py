#creating a dictionarry

student ={
    "name":"john",
    "age":21,
    "dept":"AIML",
    "Marks":[90,85,88]
}

print(student)
print(type(student))

# accessing dictionary data
print("Name:",student["name"])
print("age:",student.get("age"))

#adding a new key-value pair after creating a dictionary
student["email"]  = "ananyaharish00@gmail.com"

#modifying the dictionary
student["age"] = 18
print(student)


#removing data from the dictionary
del student["email"]
print(student)

#looping through the dictionary 
for key,value in student.items():
    print(f"{key}:{value}")

# pop
student.popitem()
print(student)

#dictionary methods
print(student.keys())
print(student.values())
print(student.items())

#dictionary comprehension
squares = {num : num**2 for num in range(1,11)}
print(squares)