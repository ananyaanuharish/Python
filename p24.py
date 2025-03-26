# user input can be read using input() in python
consumer_name = input("enter the consumer name:")
meter_no = int(input("enter the meter number:"))
unit_price = 1.5
total_units= int(input("total units:"))
bill_amt = unit_price*total_units

print("===========================================")
print("consumer name:", consumer_name)
print("meter name:", meter_no)
print("per Unit price :", unit_price)
print("total amount :", bill_amt)
print("===========================================")