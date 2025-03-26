file = open(r"C:\Users\Ananya harish\Desktop\demo.txt","a")
file.write("\nnew data added using file append")
file.close()
file = open(r"C:\Users\Ananya harish\Desktop\demo.txt","r")
data = file.readlines()
for line in data:
    print(line.strip())
file.close()