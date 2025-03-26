# Function to generate payslip
def employee_payslip(employee):
    repeat_dictionary = ("=") * 50;
    print(repeat_dictionary)
    print("   employee payslip   ")
    repeat_dictionary= ("=") * 50;
    print(repeat_dictionary)
    print(f"Employee ID   : {employee['ID']}")
    print(f"Name          : {employee['Name']}")
    print(f"Designation   : {employee['Designation']}")
    print(f"Basic Salary  : ₹{employee['Basic Salary']}")
    print(f"Tax           : ₹{employee['Tax']}")

# Employee details
employee = {
    "ID": 101,
    "Name": "Ananya A H",
    "Designation": "Software Engineer",
    "Basic Salary": 50000,
}

employee["Tax"] = 0.05 * employee["Basic Salary"]  

employee_payslip(employee)