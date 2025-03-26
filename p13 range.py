#range demo only with ending value
for i in range(5):
    print(i)

#range demo with start and ending value
for i in range(1,6):
    print(i*i)

#range demo with start, end and step value
for i in range(0,12,2):
    print(i)

# range demo with negative values start,end and step value
for i in range(10,0,-2):
    print(i)

# checking if a number is in a range
print(5 in range(1,10))
print(15 in range(1,10)) 