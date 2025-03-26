# for loop
fruits = ["Apple","Kiwi","Banana","Orange","Cherry"]
print(fruits)

for f in fruits:
    print(f)

# for using range()
for i in range(6):
    print(i)

# using dictionary
person = {"name":"Anu","age":20,"city":"Chennai"}
print(person)
for key in person:
    print(key)
else:
    print("Keys are completed")

for value in person.values():
    print(value)
else:
    print("values are completed")
    
for key,value in person.items():
    print(f"{key}:{value}")