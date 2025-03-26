#accesing list elements
emp_list = ["john",25,"dev","chennai",36000.00,25,"dev","chennai",36000.00];
print(emp_list);

print("name:",emp_list[0]," ",emp_list[5]);
print("age:",emp_list[1]);
print("department:",emp_list[2]);
print("salary:",emp_list[3]);

#slicing a list
#start And end index
print("employee 1:",emp_list[0:5]);

#only start index
print("employee 1:",emp_list[5:]);

#only end index
print("employee 1:",emp_list[:5]);

#modifying a list
emp_name=emp_list[0];
print(emp_name);
print(emp_list);
emp_list[0]="madhan"
emp_list[1] = 21;
emp_list[2]="prod";
emp_list[4]="banglore";
print(emp_list);

#append
print("before append:",emp_list);
emp_list.append("27/02/2025");
print("after append:",emp_list);

#extend for adding more values
print("before extend:",emp_list);
emp_list.extend(["01/01/2000","BE"]);
print("after extend:",emp_list);

#removing elements
print("beofre pop():",emp_list)
emp_list.pop();
print("afer pop():",emp_list)

print("Before remove():",emp_list)
emp_list.remove("chennai")
print("after remove():",emp_list)

del emp_list[5]
print(emp_list);

emp_list.clear();
print(emp_list);