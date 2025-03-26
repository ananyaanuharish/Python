# nested loop(1 for loop inside for loop and 1 while loop inside while loop)
for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()

matrix=[[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for n in row:
        print(n,end=" ")
    print()