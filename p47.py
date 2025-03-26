file = open(r"C:\Users\Ananya harish\Desktop\demo.txt","w")
file.write("""python is a simple and opensource programming language
python is a simple and opensource programming language
python is a simple and opensource programming language
python is a simple and opensource programming language
python is a simple and opensource programming language
python is a simple and opensource programming language
python is a simple and opensource programming language
python is a simple and opensource programming language""")
file.close()

file = open(r"C:\Users\Ananya harish\Desktop\demo.txt","r")
data = file.readlines()
for line in data:
    print(line.strip())
file.close()