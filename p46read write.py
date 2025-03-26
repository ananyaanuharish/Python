# write file
file = open(r"C:\Users\Ananya harish\Desktop\pyth.txt","w")
file.write("hello, this is a text file")
file.close()

#read file
file = open(r"C:\Users\Ananya harish\Desktop\pyth.txt","r")
data = file.readline()
print(data)
file.close()