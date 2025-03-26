import os
os.system('cls')

# Define (Name, ID, Age, Department)
student_records = [
    ("Ananya", "S101", 20, "AIML"),
    ("Swathi", "S102", 21, "Mechanical Engineering"),
    ("Sonu", "S103", 22, "Electrical Engineering"),
    ("Dora", "S104", 20, "Civil Engineering"),
    ("Manvi", "S105", 21, "Electronics")
]

# Writing records to the file
file= open(r"C:\Users\Ananya harish\Desktop\student_records.txt", "w")
file.write("Name, ID, Age, Department\n")
for record in student_records:
    file.write(", ".join(map(str, record)) + "\n")
print(f"Student records file '{student_records}' created successfully.")