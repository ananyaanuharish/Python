#logical operators
# and or not
x = True
y = False

print(x and y)
print(x or y)
print(not x)

a=10
b=5
#using and with if stmt
if a>5 and b<10:
    print("both conditions are true")

#using not with if stmt
if not a == 10:
    print("a is not equal to 10")
else:
    print("a is equal to 10")

#using or with if stmt
if a>5 and b<10:
    print("Atleast one condition is true")