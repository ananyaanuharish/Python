#looping through a list
fruits = ["apple","kiwi","grapes","banana","cherry"]
for i in fruits:
    print(i);

for index,i in enumerate(fruits):
    print(index,i)

#checking the membership
print("apple" in fruits);
print("data" in fruits);

#sorting a list
print("before sorting:",fruits);
fruits.sort();
print("after sorting:",fruits)

fruits.reverse()
print("after reverse:",fruits)

copy_fruits = fruits.copy()
print("list copy:",copy_fruits);
print("original fruit list:",fruits)