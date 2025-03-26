# create a set
fruits = {"apple","orange","cherry","banana","apple"}
print(fruits)
print(type(fruits))

# adding elements into set
fruits.add("kiwi")
print(fruits)

# pop() to remove the last element
fruits.pop()
print(fruits)

#remove() to remove set elements
fruits.discard("apple")
print(fruits)

#union combines all unique elements
set_A = {1,2,3,4}
set_B = {3,4,5,6,}
print("Union:", set_A | set_B)

#intersection "common elements"
print("Intersection:",set_A & set_B)

#Difference: elements in A but not in B
print("difference (A-B):", set_A - set_B)
print("difference (B-A):", set_B - set_A)

#symmetric difference : elements in either set, but not both
print("symmetric difference:", set_A ^ set_B)