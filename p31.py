# break statement
fruits = ["Apple","Kiwi","Banana","Orange","Cherry"]
print(fruits)

for f in fruits:
    print(f)

# for using range()
for i in range(10):
    print(i)
else:
    print("for loop completed")
 
# using break statement
for i in range(10):
    print(i)
    if i==5:
        break;

# using continue
for i in range(10):
    if i==6:
        continue;
    print(i)

# using pass
for i in range(10):
    if i==4:
        pass;
print(i)