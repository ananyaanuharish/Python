# os module
import os
if os.path.exists(r"C:\Users\Ananya harish\Desktop\demo.txt"):
    os.remove(r"C:\Users\Ananya harish\Desktop\demo.txt")
    print("file deleted")
else:
    print("file doesn't exit!")